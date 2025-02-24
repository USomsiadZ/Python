import mysql.connector
import xml.etree.ElementTree as ET
import PySimpleGUI as sg

def pconnect(haslo):
    if haslo == "99c9ad032e7c47ace455bd2dd7047f9c4f71639b86efdbe526a686abddecd0ce":
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
        mycursor = mydb.cursor()

    else:
        print("Haslo nie poprawne")
        exit()
    print(mydb)
    return mydb  ,mycursor
def datatable(mycursor,window,ID):
        mycursor.execute("SELECT * FROM customers")
        myresult = mycursor.fetchall()
        mr = myresult[int(ID)]
        #print(mr[13])
        
        window["input_imie"].update(mr[0])
        window["input_nazwisko"].update(mr[1])
        window["input_ulica"].update(mr[2])
        window["input_nrdomu"].update(mr[3])
        window["input_miejscowosc"].update(mr[4])
        window["input_kod"].update(mr[5])
        window["input_telefon"].update(mr[6])
        window["input_email"].update(mr[7])
        window["input_zawod"].update(mr[8])
        window["input_wiek"].update(mr[9])
        window["input_pesel"].update(mr[10])
        window["input_plec"].update(mr[11])
        window["input_miejsce"].update(mr[12])
def clear(window):
        window["input_imie"].update("")
        window["input_nazwisko"].update("")
        window["input_ulica"].update("")
        window["input_nrdomu"].update("")
        window["input_miejscowosc"].update("")
        window["input_kod"].update("")
        window["input_telefon"].update("")
        window["input_email"].update("")
        window["input_zawod"].update("")
        window["input_wiek"].update("")
        window["input_pesel"].update("")
        window["input_plec"].update("")
        window["input_miejsce"].update("")
def update(imie, Nazwisko, Ulica , Nr, Miejscowosc, Kod, Telefon, Email,Zawod,wiek,pesel,plec,Miejsce,ID,mycursor,mydb):
    #aa = int(ID) + 1
    #print(aa)
    #print("update")
    
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    myresulta = myresult[int(ID)]
    aa = myresulta[int(13)]
    bb = myresulta[int(15)]
    if bb == 1:
        sg.popup("Przedzial nie jest aktywowany")
        return 
    print(aa)
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
    mydb.commit()
    #print("update koniec")
def usun(ID,mycursor,mydb):
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    myresulta = myresult[int(ID)]
    aa = myresulta[int(13)]
    sql = "DELETE FROM customers WHERE id = '"+ str(aa) +"'"

    mycursor.execute(sql)

    mydb.commit()
    sg.popup(f"ID {aa} zostalo usuniete")
def usun2(ID,mycursor,mydb):
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    myresulta = myresult[int(ID)]
    aa = myresulta[int(13)]
    sql = "UPDATE customers SET aktywny = '1' WHERE id = '"+ str(aa) +"'"
    mycursor.execute(sql)
    mydb.commit()
    print()



        