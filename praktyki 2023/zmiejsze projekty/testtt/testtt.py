from distutils.archive_util import make_zipfile
import mysql.connector
import xml.etree.ElementTree as ET
import PySimpleGUI as sg



mytree = ET.parse('dataa.xml')
myroot = mytree.getroot()
for x in myroot.findall('passy'):
    a = x.find('host').text
    b = x.find('password').text
    c = x.find('database').text
    d = x.find('user').text
print(a,b,c,d)
    
mydb = mysql.connector.connect(
    host='localhost',
    user='Admin',
    password='toor',
    database='mydatabase'
)
mycursor = mydb.cursor()


pana = 'Polska'



sql = "INSERT INTO customers (pan) VALUES ('Polska')"
mycursor.execute(sql)
mydb.commit()