import codecs

class mock_request:
    text = "0"


class mock_request:

    def pageCounter(self):
        return 100000


    def ricoh_selfMadePage(self):
        ricohgoodpage = r"tests\mockpages\ricoh\goodtoners.html"
        #f = open(r"tests\mockpages\demofile.html", "r", encoding="utf8").read()
        f = codecs.open(ricohgoodpage,
                        'r', encoding="utf8").read()
        mockobj = mock_request()
        mockobj.text = f
        print("Ricoh Mock")
        return mockobj

    def ricoh_goodPage1(self):
        #ricohgoodpage = r"tests\mockpages\ricoh\goodtoners.html"
        ricohgoodpage = r"tests\mockpages\021221\Bort\BORT-Guido - Web Image Monitor_files\topPage.html"        
        f = codecs.open(ricohgoodpage,
                        'r', encoding="utf8").read()
        mockobj = mock_request()
        mockobj.text = f
        print("Ricoh Mock")
        return mockobj

    def ricoh2000(self):
        ricoh2000goodpage = r"tests\mockpages\ricoh\goodtoners.html"
        f = codecs.open(ricoh2000goodpage,
                        'r', encoding="utf8").read()
        mockobj = mock_request()
        mockobj.text = f
        print("Ricoh Mock")
        return mockobj
    
    
    def brother(self):
        brothergoodpage = r"xx"
        f = codecs.open(brothergoodpage,
                        'r', encoding="utf8").read()
        mockobj = mock_request()
        mockobj.text = f
        print("Ricoh Mock")
        return mockobj


    def lexmark(self):
        lexmarkgoodpage = r"xx"
        f = codecs.open(lexmarkgoodpage,
                        'r', encoding="utf8").read()
        mockobj = mock_request()
        mockobj.text = f
        print("Ricoh Mock")
        return mockobj


    def lexmarkcolor(self):
        lexmarkcolorgoodpage = r"xx"
        f = codecs.open(lexmarkcolorgoodpage,
                        'r', encoding="utf8").read()
        mockobj = mock_request()
        mockobj.text = f
        print("Ricoh Mock")
        return mockobj


    def hp(self):
        hpgoodpage = r"xx"
        f = codecs.open(hpgoodpage,
                        'r', encoding="utf8").read()
        mockobj = mock_request()
        mockobj.text = f
        print("Ricoh Mock")
        return mockobj


