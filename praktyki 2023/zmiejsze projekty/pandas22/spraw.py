import PySimpleGUI as sg
import re
import xml.etree.ElementTree as ET
def sprawdzpesel(pesel):
           
            if len(pesel) == 11:
                print("Dlugosc peselu: poprawna")
                asd = peselo(pesel)


            else:
                #print("Dlugosc peselu: nie poprawna")
                #messagebox.showinfo("Error", "Dlugosc peselu: nie poprawna")
                sg.popup("Dlugosc peselu: nie poprawna")

                return True
def sprawdz(sprawdzx,a):
        sprawdza = re.search("[0-9]", sprawdzx)
        if sprawdza:
            #print("Imie nie moze zawierac cyfr")
            #messagebox.showinfo("Error", f"{sprawdzx} nie moze zawierac cyfr")
            sg.popup(f"{a} nie moze zawierac cyfr")
        sprawdzax = re.search("^[A-Z]", sprawdzx)
        if not sprawdzax:
           #print("Imie musi sie zaczynac na duzo litere")
           #messagebox.showinfo("Error", f"{sprawdzx} musi sie zaczynac na duzo litere")
           sg.popup(f"{a} musi sie zaczynac sie na duzo litere")
           return True
def sprawdznum(sprawdzx,a):
        sprawdza = re.search("[0-9]", sprawdzx)
        if not sprawdza:
            #print("Imie nie moze zawierac cyfr")
            #messagebox.showinfo("Error", f"{sprawdzx} musi zawierac cyfr")
            sg.popup(f"{a} musi zawierac cyfr")
            return True
def sprawdzemail(sprawdzx,a):
        sprawdza = re.search("@", sprawdzx)
        if not sprawdza:
            #print("Imie nie moze zawierac cyfr")
            #messagebox.showinfo("Error", f"{sprawdzx} musi zawierac @")
            sg.popup(f"{a} musi zawierac @")
            return True
def wszystko_poprawne():
    sg.popup('Wszystko poprawne')




def peselo(a):
    pleca = "Pesel musi byc poprawny"
    wiek = "Pesel musi byc poprawny"
    pesel = a
    peselx = re.search("^[A-Z],[a-z]", a)
    if not peselx:

        if len(a) == 11:
            #tutaj
            psl = (" ".join(pesel))
            ps = psl.split()
            p0 = int(ps[0]) * 1 
            p1 = int(ps[1]) * 3 
            p2 = int(ps[2]) * 7 
            p3 = int(ps[3]) * 9 
            p4 = int(ps[4]) * 1 
            p5 = int(ps[5]) * 3 
            p6 = int(ps[6]) * 7 
            p7 = int(ps[7]) * 9 
            p8 = int(ps[8]) * 1 
            p9 = int(ps[9]) * 3 
            pp = int(p0) + int(p1)+int(p2)+int(p3)+int(p4)+int(p5)+int(p6)+int(p7)+int(p8)+int(p9)
            ppp = (" ".join(str(pp)))
            pppp = ppp.split()
            l = len(pppp)
            kk = pppp[l - 1]
            k = 10 - int(kk)
            wieka = str(ps[0]) + str(ps[1])
            if pesel.endswith(str(k)) == True:
               wiek = 23 - int(wieka)
               if k % 2 == 0:
                    pleca = "Kobieta"

               else:
                    pleca = "Mezczyzna"

            


        return pleca , wiek
