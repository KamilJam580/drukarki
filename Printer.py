import requests
from bs4 import BeautifulSoup as bs4
import json

class Printer:
    toners = {"C" : "X", "M" : "X", "Y" : "X", "K" : "X"}
    
    def __init__(self, model, name, ip):
        self.model = model
        self.name = name
        self.ip = ip
        self.pageCounter = 0
        self.pageCounter_color = 0
        self.pageCounter_bw = 0

    def IntroduceYoursfelf(self):
        message = ""
        message += "Nazwa: " + self.name + " Model: " + self.model
        message += "\nIP: " + self.ip
        print(message)

    def GetResponse(self, url):
        response = requests.get(url).text
        return response
           
    def readPageCount(self):
        return 0


class Ricoh(Printer):
    def Refresh(self): 
        self.IntroduceYoursfelf()
        #response = self.GetResponse(f"http://{self.ip}/web/guest/pl/websys/webArch/topPage.cgi").text
        self.readInkQuantity()
        self.pageCounter = self.readPageCount()
        print("\n")

    def readInkQuantity(self):
        response = requests.get(f"http://{self.ip}/web/guest/pl/websys/webArch/topPage.cgi").text
        soup = bs4(response, "html.parser")
        print("Parsed...")
        bars = soup.find_all("img", {"height": "20"})
        print("After Find...")
        self.calculateInkQuantity(bars)
        return bars
             
    def calculateInkQuantity(self, bars):
        for i, color in enumerate("KCMY"):
            try:
                x = bars[i].get("width")
                self.toners[color] = self.calculateFromPx(x)
            except:
                self.toners[color] = 0  
        return self.toners
                
    def calculateFromPx(self, x):
        return int((int(x) / 162) * 100)    
                 
    def readPageCount(self):
        response = requests.get(f"http://{self.ip}/web/guest/pl/websys/status/getUnificationCounter.cgi").text
        
        soup = bs4(response, "html.parser")
        counter = soup.find_all("tr", {"class" : "staticProp"})[1]
        
        soup = bs4(str(counter), "html.parser")
        counter = soup.find_all("td")[3].contents[0]
        
        return int(str(counter).strip())






class Ricoh2000(Ricoh):
    def Refresh(self):
        try:
            try:
                self.IntroduceYoursfelf()
                response = requests.get(f"http://{self.ip}/web/guest/pl/websys/webArch/getStatus.cgi").text
                soup = bs4(response, "html.parser")
                print("Parsed...")
                
                bars = soup.find_all("img", {"class": "ver-algn-m mgn-R5p bdr-1px-666"})
                print("After Find...")
                
                print(len(bars))
                self.calculateInkQuantity(bars)


                response = requests.get(f"http://{self.ip}/web/guest/pl/websys/status/getUnificationCounter.cgi").text
                soup = bs4(response, "html.parser")

                counter = soup.find_all("tr", {"class" : "staticProp"})[1]
                soup2 = bs4(str(counter), "html.parser")
                counter = soup2.find_all("td")[3].contents[0]
                self.pageCounter = int(str(counter).strip())
            except IndexError:
                counter = soup.find_all("tr", {"class" : "staticProp"})[2]
                self.pageCounter = int(str(counter)[176:-19].strip())

                counter = soup.find_all("td", {"width": "100", "colspan": "1"})

                self.pageCounter_color = int(str(counter[16].contents[0])) + int(str(counter[36].contents[0])) + int(str(counter[51].contents[0]))
                self.pageCounter_bw = int(str(counter[21].contents[0])) + int(str(counter[41].contents[0]))
            print("\n")
        except:
            print("Problem")



class Brother(Printer):
    def Refresh(self):
        try:
            self.IntroduceYoursfelf()

            response = requests.get(f"http://{self.ip}/general/status.html").text
            soup = bs4(response, "html.parser")
            bars = soup.find_all("img", {"class": "tonerremain"})

            for i, color in enumerate("KCMY"):
                try:
                    self.toners[color] = int((int(bars[i].get("height").replace("px", "")) / 56) * 100)
                except:
                    self.toners[color] = 0

            response = requests.get(f"http://{self.ip}/general/information.html?kind=item").text
            soup = bs4(response, "html.parser")
            counter = soup.find_all("dl", {"class": "items"})[1]
            soup = bs4(str(counter), "html.parser")
            counter = soup.find("dd").contents[0]
            self.pageCounter = int(str(counter).strip())
            print("\n")
        except:
            print("Problem")

class Lexmark(Printer):
    def Refresh(self):
        try:
            self.IntroduceYoursfelf()
            response = requests.get(f"http://{self.ip}/cgi-bin/dynamic/printer/PrinterStatus.html").text
            soup = bs4(response, "html.parser")
            bars = soup.find_all("td", {"bgcolor": "#000000"})

            for i, color in enumerate("K"):
                try:
                    self.toners[color] = int(bars[i].get("width").replace("%", ""))
                except:
                    self.toners[color] = 0
            
            self.toners["C"] = "-"
            self.toners["M"] = "-"
            self.toners["Y"] = "-"


            response = requests.get(f"http://{self.ip}/cgi-bin/dynamic/printer/config/reports/devicestatistics.html").text
            soup = bs4(response, "html.parser")
            try:
                counters = soup.find_all("p")[81].contents[0]
                self.pageCounter = int(str(counters).strip())
            except ValueError:
                self.pageCounter = 0
            print("\n")
        except:
            print("Problem")


class LexmarkColor(Printer):
    def Refresh(self):
        try:
            self.IntroduceYoursfelf()
            response = requests.get(f"http://{self.ip}/cgi-bin/dynamic/printer/PrinterStatus.html").text
            soup = bs4(response, "html.parser")
            k = soup.find("td", {"bgcolor": "#000000"})
            self.toners["K"] = int(k.get("width").replace("%", ""))

            c = soup.find("td", {"bgcolor": "#00ffff"})
            self.toners["C"] = int(c.get("width").replace("%", ""))

            m = soup.find("td", {"bgcolor": "#ff00ff"})
            self.toners["M"] = int(m.get("width").replace("%", ""))

            y = soup.find("td", {"bgcolor": "#ffff00"})
            self.toners["Y"] = int(y.get("width").replace("%", ""))
            print("\n")
        except:
            print("\n")


class HP(Printer):
    def Refresh(self):
        try:
            introduce = self.IntroduceYoursfelf()
            print(introduce)
            response = requests.get(f"http://{self.ip}").text
            soup = bs4(response, "html.parser")
            bars = str(soup.find("td", {"class": "alignRight valignTop"}).contents[0]).strip()
            bars = bars[0:bars.index("%")]
            print(len(bars))
            if bars == "--":
                self.toners["K"] = "?"

            else:
                try:
                    self.toners["K"] = int(bars)    # dostaje <10
                except:
                    print("HP EXCEPTION")
                    self.toners["K"] = 10

            self.toners["C"] = "-"
            self.toners["M"] = "-"
            self.toners["Y"] = "-"
            print("\n")
        except:
            print("\n")