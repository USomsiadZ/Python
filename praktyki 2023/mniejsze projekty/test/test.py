import re, logging, json, os

with open('data.json', 'r') as f:
  pl = json.load(f)
  plik = (pl["name"])


logging.basicConfig(filename=plik,
                    format='%(asctime)s %(message)s',
                    filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)




#g = 0
#l = 0 
a = str(input("Oblicz: "))
aa = a

a = a.replace(",",".")
a = a.replace(" * "," ; ")
a = a.replace( "+ "," , ")
a = a.replace(" ^ "," p1 ") 
a = a.replace(" - "," . ")
a = a.replace("*"," ; ")
a = a.replace("+"," , ")
a = a.replace("^"," p1 ") 
a = a.replace("-"," . ")

x = re.split(' , | ; | / | p1 | . ',a)
x1 = a.split()
if "p1" in x1:
    a5 = x1.index("p1")
if "/" in x1:
    a4 = x1.index("/")
if ";" in x1:
    a3 = x1.index(";")
if "," in x1:
    a2 = x1.index(",")
if "." in x1:
    a1 = x1.index(".")
#print(a4,"a4")
k = len(x)

  #  a3 = x1.index(";")


  #  a2 = x1.index("-")


 #   a1 = x1.index(",")
for i in range (0,k):
    #dzielenie
    if "p1" in x1:
            a1 = x1.index("p1")
            a4a = int(a1)
            f = float(x1[a4a - 1]) ** float(x1[a4a + 1])
            x1[a4a] = f
            del x1[a4a + 1]
            del x1[a4a - 1]
    elif "/" in x1:
            a4a = int(a4)
            a4 = x1.index("/")
            if float(x1[a4a + 1]) == 0:
                print("Nie mozna mozna sie dzielic przez zero")
                exit(0)
            f = float(x1[a4a - 1]) / float(x1[a4a + 1])
            x1[a4a] = f
            del x1[a4a + 1]
            del x1[a4a - 1]
    #Mnozenie
    elif ";" in x1:
            a3 = x1.index(";")
            a4a = int(a3)
            f = float(x1[a4a - 1]) * float(x1[a4a + 1])
            x1[a4a] = f
            del x1[a4a + 1]
            del x1[a4a - 1]
    
    # dodawanie
    elif "," in x1:
            a2 = x1.index(",")
            a4a = int(a2)
            f = float(x1[a4a - 1]) + float(x1[a4a + 1])
            x1[a4a] = f
            del x1[a4a + 1]
            del x1[a4a - 1]
    # odejmowanie
    elif "." in x1:
            a1 = x1.index(".")
            a4a = int(a1)
            f = float(x1[a4a - 1]) - float(x1[a4a + 1])
            x1[a4a] = f
            del x1[a4a + 1]
            del x1[a4a - 1]

os.system('cls')
print(str(aa) + " = " + str(f))
logger.info(str(aa) + " = " + str(f))
#x1.insert(0,",")
#b = 0







#for i in range (0,k):
#    if not len(x1) == 1:
#        if x1[0]==",":
#            l = l + float(x[0])
#            del x[0]
#            del x1[0]
#            if not len(x1) == 1:
#                del x1[0]
#    if not len(x1) == 1:
#        if x1[0]=="-":
#            l = l - float(x[0])
#            del x[0]
#            del x1[0]
#            if not len(x1) == 1:
#                del x1[0]
#    if not len(x1) == 1:
#        if x1[0]==";":
#            l = l * float(x[0])
#            del x[0]
#            del x1[0]
#            if not len(x1) == 1:
#                del x1[0]
#    if not len(x1) == 1:
#        if x1[0]=="/":
#            if float(x[0]) == 0:
#                print("Nieda sie dzielic przez zero")
#                exit(0)
#            l = l / float(x[0])
#            del x[0]
#            del x1[0]
#            if not len(x1) == 1:
#                del x1[0]
#    if not len(x1) == 1:
#        if x1[0]=="p1":
#            l = l ** float(x[0])
#            del x[0]
#            del x1[0]
#            if not len(x1) == 1:
#                del x1[0]
#    if not len(x1) == 1:
#        if x1[0]==".":
#            l = math.pow((l), 1.0/float(x[0]))
#            del x[0]
#            del x1[0]
#            if not len(x1) == 1:
#                del x1[0]
        
  
    

#aaa = str(aa) + " = " + str(l)
#print(aaa)
#logger.info(aaa)