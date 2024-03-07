from cProfile import label
from genericpath import exists
import mysql.connector
import pandas as pd
import xml.etree.ElementTree as ET
from tkinter import *
from  tkinter import ttk,END
from spraw import *
from logger import log
from defa import *
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg





panstwa = {'id':0,'1':'Polska','ida':0},{'id':1,'1':'Rosja','ida':1},{'id':2,'1':'Niemcy','ida':2}
pan = [panstwa[key]['1'] for key in range(len(panstwa))]
woja =  {'id':0,'1':'Mazowieckie','ida':0},{'id':0,'1':'Wielkopolskie','ida':1},{'id':0,'1':'slaskie','ida':2},{'id':1,'1':'Ruskimal','ida':0},{'id':1,'1':'Nowy Ruskimal','ida':1},{'id':1,'1':'Stary Ruskimal','ida':2},{'id':2,'1':'Niemkimal','ida':0},{'id':2,'1':'Nowy Niemkimal','ida':1},{'id':2,'1':'Stary Niemkimal','ida':2}
powi = {'id':0,'1':'a','ida':0},{'id':0,'1':'b','ida':1},{'id':0,'1':'c','ida':2},{'id':1,'1':'aa','ida':3},{'id':1,'1':'ab','ida':4},{'id':1,'1':'ac','ida':5},{'id':2,'1':'ba','ida':6},{'id':2,'1':'bb','ida':7},{'id':2,'1':'bc','ida':8},


ws  = Tk()
ws.title('Arkusz')
ws.attributes("-fullscreen", False)
ws.geometry('1800x1000')
ws['bg'] = '#AAAAAA'

mydb = def_mydb()
mycursor = mydb.cursor()    
mycursor.execute("SELECT * FROM customers WHERE aktywny = 1")
mr = mycursor.fetchall()

data(ws)
kk = cur()
#myresult = kk[0]
mycursor = kk[0]
mm = kk[1]
mycursor = mydb.cursor()    
mycursor.execute("SELECT * FROM customers WHERE aktywny = 1")
myresult = mycursor.fetchall()
game_frame = Frame(ws)


#scrollbar
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)
my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)
game_scroll.config(command=my_game.yview)


#kolumny
 
my_game['columns'] = ('player_name', 'player_Rank', 'player_states', 'player_city','miejscowosc','kod_pocztowy','telefon','email','zawod','wiek','pesel','plec','miejsce','pan','woj','pow')

mygamecolumb(my_game)
#zwykly for


obs2a = obs2(my_game)
xxx = obs2a[0]
x = obs2a[1]
mm = obs2a[2]

frame = Frame(ws,width= 1)

#labels
playername = Label(frame,text="imie")
playername.grid(row=0,column=1)

player_Rank = Label(frame,text="nazwisko")
player_Rank.grid(row=0,column=2)

player_states = Label(frame,text="ulica")
player_states.grid(row=0,column=3)

player_city = Label(frame,text="nr_domu")
player_city.grid(row=0,column=4)

miejscowosc = Label(frame,text="miejscowosc")
miejscowosc.grid(row=0,column=5)

kod_pocztowy = Label(frame,text="kod_pocztowy")
kod_pocztowy.grid(row=0,column=6)

telefon = Label(frame,text="telefon")
telefon.grid(row=0,column=7)

email = Label(frame,text="email")
email.grid(row=0,column=8)

zawod = Label(frame,text="zawod")
zawod.grid(row=0,column=9)

wiek = Label(frame,text="wiek")
wiek.grid(row=0,column=10)

pesel = Label(frame,text="pesel")
pesel.grid(row=0,column=11)

plec = Label(frame,text="plec")
plec.grid(row=0,column=12)

miejsce = Label(frame,text="miejsce")
miejsce.grid(row=0,column=13)

pan = Label(frame,text="kraj")
pan.grid(row=0,column=14)

woj1 = Label(frame,text="woj")
woj1.grid(row=0,column=15)

powa1 = Label(frame,text="powa",)
powa1.grid(row=0,column=16)



#Entry boxes

playername_entry = Entry(frame,width= 15)
playername_entry.grid(row=1,column=1)

playerrank_entry = Entry(frame,width= 15)
playerrank_entry.grid(row=1,column=2)

player_states_entry = Entry(frame,width= 15)
player_states_entry.grid(row=1,column=3)

player_city_entry = Entry(frame,width= 15)
player_city_entry.grid(row=1,column=4)

miejscowosc_entry = Entry(frame,width= 15)
miejscowosc_entry.grid(row=1,column=5)

kod_pocztowy_entry = Entry(frame,width= 15)
kod_pocztowy_entry.grid(row=1,column=6)

telefon_entry = Entry(frame,width= 15)
telefon_entry.grid(row=1,column=7)

email_entry = Entry(frame,width= 15)
email_entry.grid(row=1,column=8)

zawod_entry = Entry(frame,width= 15)
zawod_entry.grid(row=1,column=9)

wiek_entry = Entry(frame,width= 15)
wiek_entry.grid(row=1,column=10)

pesel_entry = Entry(frame,width= 15)
pesel_entry.grid(row=1,column=11)

plec_entry = Entry(frame,width= 15)
plec_entry.grid(row=1,column=12)

miejsce_entry = Entry(frame,width= 15)
miejsce_entry.grid(row=1,column=13)

pan_entry = Entry(frame,width= 15)
pan_entry.grid(row=1,column=14)

woj_entry = Entry(frame,width= 15)
woj_entry.grid(row=1,column=15)

pow_entry = Entry(frame,width= 15)
pow_entry.grid(row=1,column=16)

my_game.pack()
frame.pack(pady=20)
game_frame.pack()


#Select Record
def select_record():
    #clear entry boxes
    playername_entry.delete(0,END)
    playerrank_entry.delete(0,END)
    player_states_entry.delete(0,END)
    player_city_entry.delete(0,END)
    miejscowosc_entry.delete(0,END)
    kod_pocztowy_entry.delete(0,END)
    telefon_entry.delete(0,END)
    email_entry.delete(0,END)
    zawod_entry.delete(0,END)
    wiek_entry.delete(0,END)
    pesel_entry.delete(0,END)
    plec_entry.delete(0,END)
    miejsce_entry.delete(0,END)
    pan_entry.delete(0,END)
    woj_entry.delete(0,END)
    pow_entry.delete(0,END)


    #grab record
    selected=my_game.focus()
    #grab record values
    values = my_game.item(selected,'values')
    #temp_label.config(text=selected)

    #output to entry boxes
    playername_entry.insert(0,values[0])
    playerrank_entry.insert(0,values[1])
    player_states_entry.insert(0,values[2])
    player_city_entry.insert(0,values[3])
    miejscowosc_entry.insert(0,values[4])
    kod_pocztowy_entry.insert(0,values[5])
    telefon_entry.insert(0,values[6])
    email_entry.insert(0,values[7])
    zawod_entry.insert(0,values[8])
    wiek_entry.insert(0,values[9])
    pesel_entry.insert(0,values[10])
    plec_entry.insert(0,values[11])
    miejsce_entry.insert(0,values[12])
    m13 = values[13]
    m14 = values[14]
    m15 = values[15]
    i = m13
    k = m14
    x = 1
    pam = [panstwa[key]['1'] for key in range(len(panstwa))]
    if i in [pam[i] for i in range(len(panstwa))]:

        
        x = pam.index(i)
        m13 = panstwa[x]['id']

    woji = [woja[key]['1'] for key in range(len(woja))]

    if k in [woji[k] for k in range(len(woji))]:

        
        xx = woji.index(k)

        m14= woja[xx]['ida']







    pan_entry.insert(0,m13)
    woj_entry.insert(0,m14)
    pow_entry.insert(0,m15)



#save Record
def update_record():
    #spraw()
    selected=my_game.focus()
    #save new data 
    my_game.item(selected,text="",values=(playername_entry.get(),playerrank_entry.get(),player_states_entry.get(),player_city_entry.get(),miejscowosc_entry.get(),kod_pocztowy_entry.get(),telefon_entry.get(),email_entry.get(),zawod_entry.get(),wiek_entry.get(),pesel_entry.get(),plec_entry.get(),miejsce_entry.get(),pan_entry.get(),woj_entry.get(),pow_entry.get() ))
   
   #clear entry boxes
    playername_entry.delete(0,END)
    playerrank_entry.delete(0,END)
    player_states_entry.delete(0,END)
    player_city_entry.delete(0,END)
    miejscowosc_entry.delete(0,END)
    kod_pocztowy_entry.delete(0,END)
    telefon_entry.delete(0,END)
    email_entry.delete(0,END)
    zawod_entry.delete(0,END)
    wiek_entry.delete(0,END)
    pesel_entry.delete(0,END)
    plec_entry.delete(0,END)
    miejsce_entry.delete(0,END)
    pan_entry.delete(0,END)
    woj_entry.delete(0,END)
    pow_entry.delete(0,END)

#Buttons
def updatesql():
    update_record()
    #aa = int(ID) + 1

    selected=my_game.focus()
    #grab record values
    values = my_game.item(selected,'values')
    imie = values[0]
    Nazwisko = values[1]
    Ulica = values[2]
    Nr = values[3]
    Miejscowosc = values[4]
    Kod = values[5]
    Telefon = values[6]
    Email = values[7]
    Zawod = values[8]
    wiek = values[9]
    pesel = values[10]
    plec = values[11]
    Miejsce = values[12]
    pan = values[13]
    woj1 = values[14]
    powaa = values[15]

    mycursor.execute("SELECT * FROM customers WHERE aktywny = 1")
    myresult = mycursor.fetchall()
    ID = int(my_game.focus()) - 1

    
    myresulta = myresult[int(ID)]
    aa = myresulta[int(13)]
    sql = "UPDATE customers SET imie = '" + imie + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET nazwisko = '" + Nazwisko + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET Ulica = '" + Ulica + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET Nr_domu = '" + Nr + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET Miejscowosc = '" + Miejscowosc + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET Kod_pocztowy = '" + Kod + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET Telefon = '" + Telefon + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET Email = '" + Email + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET Zawod = '" + Zawod + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET Wiek = '" + wiek + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET Pesel = '" + pesel + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET Plec = '" + plec + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET Miejsce_urodzenia = '" + Miejsce + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET kraj = '" + pan + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET woj = '" + woj1 + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)
    sql = "UPDATE customers SET pow = '" + powaa + "' WHERE id = '" + str(aa) + "' "
    mycursor.execute(sql)



    mydb.commit()
    ods(my_game)
def usun2():
    ID = my_game.focus()
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    myresulta = myresult[int(ID)]
    aa = myresulta[int(13)]
    sql = "UPDATE customers SET aktywny = '0' WHERE id = '"+ str(aa) +"'"
    mycursor.execute(sql)
    mydb.commit()
    ods(my_game)
def spraw():
        values=(playername_entry.get(),playerrank_entry.get(),player_states_entry.get(),player_city_entry.get(),miejscowosc_entry.get(),kod_pocztowy_entry.get(),telefon_entry.get(),email_entry.get(),zawod_entry.get(),wiek_entry.get(),pesel_entry.get(),plec_entry.get(),miejsce_entry.get())
        #02070803628                 k
        imie = values[0]
        Nazwisko = values[1]
        Nr = values[3]
        Kod = values[5]
        Telefon = values[6]
        Email = values[7]
        pesel = values[10]
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
                                if xx == None:
                                    #xx = wszystko_poprawne()
                                    asd = peselo(pesel)
                                    wiek_entry.delete(0,END)
                                    plec_entry.delete(0,END)
                                    wiek_entry.insert(0,values[9])
                                    plec_entry.insert(0,values[11])
                                    return True

def spraw2():
    #02070803628                 k
        values=(playername_entry.get(),playerrank_entry.get(),player_states_entry.get(),player_city_entry.get(),miejscowosc_entry.get(),kod_pocztowy_entry.get(),telefon_entry.get(),email_entry.get(),zawod_entry.get(),wiek_entry.get(),pesel_entry.get(),plec_entry.get(),miejsce_entry.get())
        imie = values[0]
        Nazwisko = values[1]
        Nr = values[3]
        Kod = values[5]
        Telefon = values[6]
        Email = values[7]
        pesel = values[10]
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
                                if xx == None:
                                    #xx = wszystko_poprawne()
                                    asd = peselo(pesel)
                                    wiek_entry.delete(0,END)
                                    plec_entry.delete(0,END)
                                    wiek_entry.insert(0,values[9])
                                    plec_entry.insert(0,values[11])
                                    
                                    return True,asd[0],asd[1]
def logger():
    kk = spraw2()
    if kk[0] == None:
        print("Nie poprawne")
        return
    selected=my_game.focus()
    values=(playername_entry.get(),playerrank_entry.get(),player_states_entry.get(),player_city_entry.get(),miejscowosc_entry.get(),kod_pocztowy_entry.get(),telefon_entry.get(),email_entry.get(),zawod_entry.get(),kk[1],pesel_entry.get(),kk[2],miejsce_entry.get(),pan_entry.get(),woj_entry.get(),pow_entry.get() )
    imie = values[0]
    Nazwisko = values[1]
    Ulica = values[2]
    Nr = values[3]
    Miejscowosc = values[4]
    Kod = values[5]
    Telefon = values[6]
    Email = values[7]
    Zawod = values[8]
    pesel = values[10]
    Miejsce = values[12]
    pan = values[13]
    woj1 = values[14]
    powa = values[15]
    log(imie,Nazwisko,Ulica,Nr,Miejscowosc,Kod,Telefon,Email,Zawod,pesel,Miejsce,mycursor,str(kk[2]),str(kk[1]),mydb,pan,woj1,powa)
    ods(my_game)
    playername_entry.delete(0,END)
    playerrank_entry.delete(0,END)
    player_states_entry.delete(0,END)
    player_city_entry.delete(0,END)
    miejscowosc_entry.delete(0,END)
    kod_pocztowy_entry.delete(0,END)
    telefon_entry.delete(0,END)
    email_entry.delete(0,END)
    zawod_entry.delete(0,END)
    wiek_entry.delete(0,END)
    pesel_entry.delete(0,END)
    plec_entry.delete(0,END)
    miejsce_entry.delete(0,END)
    pan_entry.delete(0,END)
    woj_entry.delete(0,END)
    pow_entry.delete(0,END)

def usun():
    ID = my_game.focus()
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    myresulta = myresult[int(ID) - 1]
    aa = myresulta[int(13)]

    sql = "DELETE FROM customers WHERE id = '"+ str(aa) +"'"

    mycursor.execute(sql)

    mydb.commit()
    ods(my_game)


select_button = Button(ws,text="Wybierz", command=select_record)
select_button.pack(pady = 10,side = LEFT)

usun_button = Button(ws,text="usun",command=usun)
usun_button.pack(pady = 10,side = LEFT)

usun2_button = Button(ws,text="usun 2",command=usun2)
usun2_button.pack(pady = 10,side = LEFT)

#selected=my_game.focus()
#values = my_game.item(selected,'values')

updatesql = Button(ws,text="update",command=updatesql)
updatesql.pack(pady = 10,side = LEFT)

logsql = Button(ws,text="Dodaj",command=logger)
logsql.pack(pady = 10,side = LEFT)

#odsaa = Button(ws,text="ods",command=ods(my_game))
#odsaa.pack(pady = 10,side = LEFT)

asd = Button(ws,text="exit",command=exit)
asd.pack(pady = 10,side = LEFT)


def tick():
    ods(my_game)
    my_game.after(10000, tick)
#tick()
ws.mainloop()

