import os,time
seconds = time.time()
lt = time.ctime(seconds) + ": "

print("Kalkulator")
print("1 Dodawanie")
print("2 Odejmowanie")
print("3 Mnozenie ")
print("4 Dzielenie")
print("5 logi")
def odejmowanie():
    os.system('cls')
    a = int(input("Pierwsza liczba: "))
    b = int(input("Druga liczba: "))
    c = a - b
    
    file1 = open("logi.txt", "a") 
    d = lt + str(a) + " - " + str(b) + " = " + str(c)  + '\n'
    file1.write(d)
    file1.close()
    return c
def dodawanie():
    os.system('cls')
    a = int(input("Pierwsza liczba: "))
    b = int(input("Druga liczba: "))
    c = a + b
    
    file1 = open("logi.txt", "a") 
    d = lt + str(a) + " + " + str(b) + " = " + str(c)  + '\n'
    file1.write(d)
    file1.close()
    return c
def mnozenie():
    os.system('cls')
    a = int(input("Pierwsza liczba: "))
    b = int(input("Druga liczba: "))
    c = a * b
    
    file1 = open("logi.txt", "a") 
    d = lt + str(a) + " * " + str(b) + " = " + str(c) + '\n'
    file1.write(d)
    file1.close()
    return c
def dzielenie():
    os.system('cls')
    a = int(input("Pierwsza liczba: "))
    b = int(input("Druga liczba: "))
    if b == 0:
        print("Nie mozna dzielic przez 0")
    c = a / b
    file1 = open("logi.txt", "a") 
    d = lt + str(a) + " / " + str(b) + " = " + str(c) + '\n'
    file1.write(d)
    file1.close()
    return c
def logi():
    os.system('cls')
    file1 = open("logi.txt", "r")
    print(file1.read())

g = int(input())

if g == 1:
    c = dodawanie()
elif g == 2:
    c = odejmowanie()
elif g == 3:
    c = mnozenie()
elif g == 4:
    c = dzielenie()
elif g == 5:
    c = logi()
else: print("Nie prawidlowy numer")
if g != 5:
    print("Wynik: ",c)

