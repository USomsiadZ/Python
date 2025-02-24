import logging
from pconnect import pconnect
import mysql.connector
import xml.etree.ElementTree as ET
import PySimpleGUI as sg



def log(imie,Nazwisko,Ulica,Nr,Miejscowosc,Kod,Telefon,Email,Zawod,pesel,Miejsce,haslo,mycursor,wiek,plec,mydb,al,ala,alc):


    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    print("Zapisywanie do pliku log")
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
    i = 1
    sql = "INSERT INTO customers (imie, nazwisko, ulica , nr_domu, miejscowosc, kod_pocztowy, telefon, email,zawod,wiek,pesel,plec,miejsce_urodzenia,kraj,woj,pow,aktywny) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (imie,Nazwisko,Ulica,Nr,Miejscowosc,Kod,Telefon,Email,Zawod, wiek ,pesel,plec,Miejsce,al,ala,alc,i)
    #sql = "INSERT INTO customers (imie) VALUES (%s)"
    #val = ("John")
    mycursor.execute(sql, val)
    mydb.commit()
    sg.popup("Zapisano do logow i sql")