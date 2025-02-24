import select
import PySimpleGUI as sg
import logging, re,time
from spraw import *
from pconnect import pconnect, datatable, clear,update,usun,usun2
from logger import log
from layout import layout
from hashlib import sha256
privatekey = "ZPM Export Import JBB Jozef Baldyga"
#input_ = str(input("Podaj haslo: ")) + privatekey
input_ = 'root' + privatekey
haslo = sha256(input_.encode('utf-8')).hexdigest()

imie = " "
Nazwisko = " "
Ulica = " "
Nr = " "
Miejscowosc = " "
Kod = " "
Telefon = " "
Email = " "
Zawod = " "
pesel = " "
Miejsce = " "
wiek =" "
plec = " "
#02070803628                 k
#pana = {1: 'Polska' , 2: 'Niemcy', 3: 'Rosja'}
#keys = [1,2,3]
#pan = [pana[key] for key in keys]
xx  = 0
woj_visib = False
#zadeklaruj tablice gdzie kluczem bedzie id a wartoscio bedzie napis
panstwa = {'id':0,'1':'Polska'},{'id':1,'1':'Rosja'},{'id':2,'1':'Niemcy'}
print(panstwa[0])
  

pan = [panstwa[key]['1'] for key in range(len(panstwa))]
woja =  {'id':0,'1':'Mazowieckie','ida':0},{'id':0,'1':'Wielkopolskie','ida':1},{'id':0,'1':'slaskie','ida':2},{'id':1,'1':'Ruskimal','ida':0}

powi = {'id':0,'1':'a','ida':0},{'id':0,'1':'b','ida':1},{'id':0,'1':'c','ida':2},{'id':1,'1':'aa','ida':3},{'id':1,'1':'ab','ida':4},{'id':1,'1':'ac','ida':5},{'id':2,'1':'ba','ida':6},{'id':2,'1':'bb','ida':7},{'id':2,'1':'bc','ida':8},
#print(powi)
keyo = []
powii = [powi[key]['1'] for key in range(len(powi))]
    
def woj(a):
    xx  = 0
    keyo = []  
    for i in woja:
        if i['id']==a:
            keyo.insert(xx, xx)
        xx = xx + 1
    woj = [woja[key]['1'] for key in keyo]
    wojid = [woja[key]['ida'] for key in keyo]

    return woj,wojid


def powa(a):
    xx  = 0
    keyo = []  
    for i in powi:
        if i['id']==a:
            keyo.insert(xx, xx)
        xx = xx + 1
    powaa = [powi[key]['1'] for key in keyo]
    powaaid = [powi[key]['ida'] for key in keyo]

    return powaa,powaaid

#value = '1'
#print([key for key in woja.items() if key[1] == value][0][0])



data = pconnect(haslo)
logging.basicConfig(filename="log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')



asd = [0,0]

window = sg.Window('Formularz zgloszeniowy', layout(pan,'0','0' ))
f = 0
ll = 1
while True:
    event, x = window.read()
    #def layout():
    #    layout = [  
    #        [sg.Text('Imie              ',size=(15, 1)), sg.InputText(key="input_imie")]]
    #    return layout
    #window = sg.Window('Formularz zgloszeniowy', layout(), )
    imie = x["input_imie"]
    Nazwisko = x["input_nazwisko"]
    Ulica = x["input_ulica"]
    Nr = x["input_nrdomu"]
    Miejscowosc = x["input_miejscowosc"]
    Kod = x["input_kod"]
    Telefon = x["input_telefon"]
    Email = x["input_email"]
    Zawod = x["input_zawod"]
    pesel = x["input_pesel"]
    Miejsce = x["input_miejsce"]
    #ID = x["input_id"]
    wiek = x["input_wiek"]
    plec = x["input_plec"]


    if event == "Sprawdz pesel":
        sprawdzpesel(pesel)

    if event == "Auto wiek":
        asd = peselo(pesel)
        if not asd[0] == 0:
            window["input_wiek"].update(asd[0])
    if event == "Auto plec":
        asd = peselo(pesel)
        if not asd[1] == 0:
            window["input_plec"].update(asd[1])
    if event == 'Wyslij':
        log(imie,Nazwisko,Ulica,Nr,Miejscowosc,Kod,Telefon,Email,Zawod,pesel,Miejsce,haslo,data[1],wiek,plec,data[0],al,ala,alc)
    if event == "Wyslija":
        xx = sprawdzpesel(pesel)
        if xx == None:
            xx = sprawdz(imie,"Imie")
            if xx == None:
                xx = sprawdz(Nazwisko,"Nazwisko")
                if xx == None:
                    xx = sprawdznum(Kod,"Kod pocztowy")
                    if xx == None:
                        xx = sprawdznum(Nr,"Numer domu")
                        if xx == None:
                            xx = sprawdznum(Telefon,"Telefon")
                            if xx == None:
                                xx = sprawdzemail(Email,"Email")
                                log(imie,Nazwisko,Ulica,Nr,Miejscowosc,Kod,Telefon,Email,Zawod,pesel,Miejsce,haslo,data[1],wiek,plec,data[0],al,ala,alc)
    if event == "Data table":
            datatable(data[1],window,ID)
    if event == "Clear":
            clear(window)
    if event == "Update":
        update(imie, Nazwisko, Ulica , Nr, Miejscowosc, Kod, Telefon, Email,Zawod,wiek,pesel,plec,Miejsce,ID,data[1],data[0])
    if event == "Usun":
        usun(ID,data[1],data[0])
    if event == "Usun2":
        usun2(ID,data[1],data[0])


                     

    if event == "Zapisz do log":
        log(imie,Nazwisko,Ulica,Nr,Miejscowosc,Kod,Telefon,Email,Zawod,pesel,Miejsce,haslo,data[1],wiek,plec,data[0],al,ala,alc)
    if event == 'input_kraj':
        event = 'test'
    if event == 'input_woj':
        event = 'test'
    if event == 'input_pow':
        event = 'test'
        
        print('ijsnfddsibfihjbfsnjbfdnjbndfnkjbfdknk')
    if event == 'test':
        combo = x['input_kraj']
        comba = x['input_woj']
        com = x['input_pow']
        imie = x["input_imie"]
        Nazwisko = x["input_nazwisko"]
        Ulica = x["input_ulica"]
        Nr = x["input_nrdomu"]
        Miejscowosc = x["input_miejscowosc"]
        Kod = x["input_kod"]
        Telefon = x["input_telefon"]
        Email = x["input_email"]
        Zawod = x["input_zawod"]
        pesel = x["input_pesel"]
        Miejsce = x["input_miejsce"]
        wiek = x["input_wiek"]
        plec = x["input_plec"]
        if not combo == " ":
            on = False
            al = pan.index(combo)
            if not comba == " ":
                ala = woj(al)[0].index(comba)
                if not com == " ":
                    alc = powii.index(com)
                    print(al)
                    print(ala)
                    print(alc)
            else:
                ala = '0'
              # use the combo key
            #window['input_woj'].update(values=woj)
            #print(combo)

            window.close()
            window = sg.Window('Formularz zgloszeniowy', layout(pan,woj(al),powa(ala)   )).Finalize()

            window['input_woj'].Update(visible=True)
            window['input_woj'].unhide_row()
            window['input_kraj'].Update(disabled = True)
            if not comba == " ":
                if woj_visib:
                    window['input_pow'].Update(visible=True)
                    window['input_woj'].Update(disabled = True)
                    window['input_pow'].unhide_row()
                    if not com == " ":
                        window['input_pow'].Update(disabled = True)

            woj_visib = True


            window["input_imie"].update(imie)
            window["input_nazwisko"].update(Nazwisko)
            window["input_ulica"].update(Ulica)
            window["input_nrdomu"].update(Nr)
            window["input_miejscowosc"].update(Miejscowosc)
            window["input_kod"].update(Kod)
            window["input_telefon"].update(Telefon)
            window["input_email"].update(Email)
            window["input_zawod"].update(Zawod)
            window["input_pesel"].update(pesel)
            window["input_miejsce"].update(Miejsce)
            window["input_wiek"].update(wiek)
            window["input_plec"].update(plec)
            window["input_kraj"].update(combo)
            window["input_woj"].update(comba)
            window["input_pow"].update(com)
            
            

    if event == sg.WIN_CLOSED:
        break
print(window)
window.close()