from Printer import *


bort = Ricoh("Ricoh MP C2051", "BORT Guido", "192.168.20.28")
di = Brother("Brother MFC-9340CDW", "Informatycy", "192.168.20.23")
dzp = Brother("Brother DCP-L8400CDN", "DZP (Agricoli)", "192.168.20.29")
digi = Lexmark("Lexmark MS415dn", "DigiLexmark", "192.168.20.81")
wolnosci = Ricoh2000("Ricoh MP C2003", "Wolnosci 402 parter", "192.168.20.52")
dyspozytor = HP("HP M402dne", "Dyspozytor", "192.168.20.130")
gazobudowa = Ricoh2000("Ricoh MP C2011", "Gazobudowa", "192.168.20.101")
bortHP = HP("HP M402dne", "KasaGuido", "192.168.20.19")
kasaLaznia = Brother("Brother DCP-L8400CDN", "KasaLaznia", "192.168.20.31")
kasaMiarki = Brother("Brother DCP-L8400CDN", "KasaMiarki", "192.168.20.32")
kasaLuiza = Brother("Brother DCP-L8400CDN", "KasaLuiza(P12C)", "192.168.20.33")
ksiegowoscDuza = Ricoh2000("Ricoh IM C2000", "Ksiegowosc-duza", "192.168.20.43")
ksiegowoscMala = Lexmark("Lexmark MS312dn", "Ksiegowosc-mala", "192.168.20.24")
miarki = Ricoh2000("Ricoh MP C2003", "Miarki", "192.168.20.51")
bklajmon = Lexmark("Lexmark MS610dn", "Biuro-bklajmon(Gazobudowa)", "192.168.20.50")
mieszkanie = Ricoh2000("Ricoh MP C2011", "Mieszkanie", "192.168.20.35")
reok = Ricoh2000("Ricoh IM C2000", "Agricoli REOK", "192.168.20.44", )
sekretariat = Ricoh2000("Ricoh IM C2000", "Agricoli sekretariat", "192.168.20.42")
wolnosciPietro = Ricoh2000("Ricoh IM C2000", "Wolnosci 402 pietro", "192.168.20.45")
guidoKasy = LexmarkColor("Lexmark X950", "Bort GUIDO Kasy", "192.168.20.20")
graficy = Ricoh2000("Ricoh IM C2500", "Graficy (Agricoli)", "192.168.20.47")
skansen = Ricoh2000("Ricoh MP C2003", "Skansen (P12C)", "192.168.20.67")


all_printers = [bort, di, dzp, digi, wolnosci, dyspozytor, gazobudowa, bortHP, kasaLaznia, kasaMiarki, kasaLuiza, ksiegowoscDuza, ksiegowoscMala, miarki, bklajmon, mieszkanie, reok, sekretariat
, wolnosciPietro
, guidoKasy
,graficy
,skansen
]

if __name__ == "__main__":
    data = []
    for i, printer in enumerate(all_printers):
        printer.Refresh()
        data.append({"id" : i, "name" : printer.name, "model" : printer.model, "IP" : printer.ip, "C" : printer.toners["C"], "M" : printer.toners["M"], "Y" : printer.toners["Y"], "K" : printer.toners["K"], "AllPages" : printer.pageCounter, "PagesBW" : printer.pageCounter_bw, "PagesColor": printer.pageCounter_color})
    
    from datetime import date
    today = date.today()
    print("Today's date:", today)

    print (data)
    data = {"printers" : data}
    #with open("data.json", "w") as w:
    with open(r"/var/www/html/data.json", "w") as w:
        json.dump(data, w)

