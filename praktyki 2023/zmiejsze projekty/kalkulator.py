import math
a = str(input("Pierwsza liczba: "))
doda = a.count("+")
odej = a.count("-")
mnoz = a.count("*")
dziel = a.count("/")
potegi = a.count("^")
pierw = a.count("p")
end = len(a)
b = a.split()
print(b)
def doda2():
    j = a[0:a.find("+") - 1]
    j2 = a[a.find("+") + 2:end] 
    print(int(j) + int(j2))
def odej2():
    j = a[0:a.find("-") - 1]
    j2 = a[a.find("-") + 2:end] 
    print(int(j) - int(j2))
def mnoz2():
    j = a[0:a.find("*") - 1]
    j2 = a[a.find("*") + 2:end] 
    print(int(j) * int(j2))
def dziel2():
    j = a[0:a.find("/") - 1]
    j2 = a[a.find("/") + 2:end]
    if int(j2)==0:
        print("Nie mozna dzilic przez 0")
        exit()
    print(int(j) / int(j2))
def potegi2():
    j = a[0:a.find("^") - 1]
    j2 = a[a.find("^") + 2:end] 
    print(int(j) ** int(j2))
def pierw2():
    j = a[0:a.find("p") - 1]
    j2 = a[a.find("p") + 2:end] 
    print(math.pow(int(j), 1.0/int(j2)))
if doda > 0:
    doda2()
elif odej > 0:
    odej2()
elif mnoz > 0:
    mnoz2()
elif dziel > 0:
    dziel2()
elif potegi > 0:
    potegi2()
elif pierw > 0:
    pierw2()

