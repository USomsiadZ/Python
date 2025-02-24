import mysql.connector
import pandas as pd
import xml.etree.ElementTree as ET
from tkinter import *
from  tkinter import ttk,END
from spraw import *
from logger import log
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


panstwa = {'id':0,'1':'Polska','ida':0},{'id':1,'1':'Rosja','ida':1},{'id':2,'1':'Niemcy','ida':2}
pan = [panstwa[key]['1'] for key in range(len(panstwa))]
woja =  {'id':0,'1':'Mazowieckie','ida':0},{'id':0,'1':'Wielkopolskie','ida':1},{'id':0,'1':'slaskie','ida':2},{'id':1,'1':'Ruskimal','ida':0},{'id':1,'1':'Nowy Ruskimal','ida':1},{'id':1,'1':'Stary Ruskimal','ida':2},{'id':2,'1':'Niemkimal','ida':0},{'id':2,'1':'Nowy Niemkimal','ida':1},{'id':2,'1':'Stary Niemkimal','ida':2}
powi = {'id':0,'1':'a','ida':0},{'id':0,'1':'b','ida':1},{'id':0,'1':'c','ida':2},{'id':1,'1':'aa','ida':3},{'id':1,'1':'ab','ida':4},{'id':1,'1':'ac','ida':5},{'id':2,'1':'ba','ida':6},{'id':2,'1':'bb','ida':7},{'id':2,'1':'bc','ida':8},
def ods(my_game):
    my_game.delete(*my_game.get_children())
    obs2(my_game)
    return
def cur():
    mydb = def_mydb()
    mycursor = mydb.cursor()    
    mycursor.execute("SELECT * FROM customers WHERE aktywny = 1")
    return mycursor, mydb

def def_mydb():
    mytree = ET.parse('dataa.xml')
    myroot = mytree.getroot()
    for x in myroot.findall('passy'):
        a = x.find('host').text
        b = x.find('password').text
        c = x.find('database').text
        d = x.find('user').text
    mydb = mysql.connector.connect(
      host=a,
      user=d,
      password=b,
      database=c
    )
    return mydb

def mygamecolumb(my_game):
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("player_name",anchor=CENTER,width=125)
    my_game.column("player_Rank",anchor=CENTER,width=125)
    my_game.column("player_states",anchor=CENTER,width=125)
    my_game.column("player_city",anchor=CENTER,width=125)
    my_game.column("miejscowosc",anchor=CENTER,width=125)
    my_game.column("kod_pocztowy",anchor=CENTER,width=125)
    my_game.column("telefon",anchor=CENTER,width=125)
    my_game.column("email",anchor=CENTER,width=125)
    my_game.column("zawod",anchor=CENTER,width=125)
    my_game.column("wiek",anchor=CENTER,width=125)
    my_game.column("pesel",anchor=CENTER,width=125)
    my_game.column("plec",anchor=CENTER,width=125)
    my_game.column("wiek",anchor=CENTER,width=90)
    my_game.column("miejsce",anchor=CENTER,width=110)
    my_game.column("pan",anchor=CENTER,width=90)
    my_game.column("woj",anchor=CENTER,width=90)
    my_game.column("pow",anchor=CENTER,width=90)



    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("player_name",text="Imie",anchor=CENTER)
    my_game.heading("player_Rank",text="Nazwisko",anchor=CENTER)
    my_game.heading("player_states",text="ulica",anchor=CENTER)
    my_game.heading("player_city",text="numer domu",anchor=CENTER)
    my_game.heading("miejscowosc",text="miejscowosc",anchor=CENTER)
    my_game.heading("kod_pocztowy",text="kod_pocztowy",anchor=CENTER)
    my_game.heading("telefon",text="telefon",anchor=CENTER)
    my_game.heading("email",text="email",anchor=CENTER)
    my_game.heading("zawod",text="zawod",anchor=CENTER)
    my_game.heading("wiek",text="wiek*",anchor=CENTER)
    my_game.heading("pesel",text="pesel",anchor=CENTER)
    my_game.heading("plec",text="plec*",anchor=CENTER)
    my_game.heading("miejsce",text="miejsce_urodzenia",anchor=CENTER)
    my_game.heading("pan",text="panstwo",anchor=CENTER)
    my_game.heading("woj",text="woj",anchor=CENTER)
    my_game.heading("pow",text="pow",anchor=CENTER)

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

def obs2(my_game):
    mydb = def_mydb()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customers WHERE aktywny = 1")
    myresult = mycursor.fetchall()
    mm = myresult[0]
    xxx = 0
    kk = []
    ll = 0
    for xx in myresult:
        xxx = xxx + 1
    xxx = xxx - 1
    x = 0
    while x <= xxx:
        mm = myresult[x]
        m16 = mm[16]
        m17 = mm[17]
        m18 = mm[18]
        i = mm[16]
        i2 = mm[17]
        i3 = mm[18]



        if i in [panstwa[i]['id'] for i in range(len(panstwa))]:
                m16 = panstwa[i]['1'] 
                m16a = panstwa[i]['ida']
        for i22 in woj(0)[1]:#0,1,2
            if i2 in woj(i22)[1]:
                m17 = woj(m16a)[0][mm[17]]
                        

                    








                if i3 in [powi[i3]['id'] for i3 in range(len(powa(0)[0]))]:
                    m18 = powi[i3]['1']

        my_game.insert(parent='',iid = x + 1,index=x + 1,text='',
        values = (mm[0],mm[1],mm[2], mm[3], mm[4],mm[5],mm[6],mm[7],mm[8],mm[9],mm[10],mm[11],mm[12],m16,m17,m18))

        x = x + 1
    return xxx,x,mm

def data(ws):
    data = pd.read_sql("select * from mydatabase.customers", def_mydb());
    df2x = data.pivot_table(index = ['Wiek'], aggfunc ='size')
    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, ws)
    bar1.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH)                    
    df2x.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Wiek')















