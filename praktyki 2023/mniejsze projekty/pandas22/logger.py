import logging
import mysql.connector
import xml.etree.ElementTree as ET
import PySimpleGUI as sg


def pconnect():
    
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
        return mydb  ,mycursor
def log(imie,Nazwisko,Ulica,Nr,Miejscowosc,Kod,Telefon,Email,Zawod,pesel,Miejsce,mycursor,wiek,plec,mydb,Pans,woj,powa):


    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)


    logger.info("Imie: " + imie)
    logger.info("Nazwisko: " + Nazwisko)
    logger.info("Ulica: " + Ulica)
    logger.info("Nr domu: " + Nr)
    logger.info("Kod pocztowy: " + Kod)
    logger.info("Telefon: " + Telefon)
    logger.info("Email: " + Email)
    logger.info("Zawod: " + Zawod)
    logger.info("Wiek: " + wiek)
    logger.info("Plec: " + plec)
    logger.info("pesel: " + pesel)
    logger.info("Miejsce: " + Miejsce)
    sql = "INSERT INTO customers (imie, nazwisko, ulica , nr_domu, miejscowosc, kod_pocztowy, telefon, email,zawod,wiek,pesel,plec,miejsce_urodzenia,aktywny,kraj,woj,pow) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (imie,Nazwisko,Ulica,Nr,Miejscowosc,Kod,Telefon,Email,Zawod, wiek ,pesel,plec,Miejsce, "1", Pans, woj, powa)
    mycursor.execute(sql, val)
    mydb.commit()