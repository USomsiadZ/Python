import tkinter as tk
from tkinter import Listbox, ttk, END,messagebox
from tkcalendar import DateEntry
import mysql.connector,sys
from hashlib import sha256
#Połączenie mysql
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="toor",
        password="ZAQ!2wsx",
        database="Database"
    )
except:
    messagebox.showerror("Error","Nie można się połączyć z serverem")
    sys.exit()
cursor = mydb.cursor()

#GUI
root = tk.Tk()
root.geometry("800x600")
root.title("Menu")
email_nick = None

#funkcje
class GUI_function:
    def __init__(self,root):
        self.root = root
        pass
    def forget_allwidget(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        
    def pack_widgets(self,widgets=None,forgetallwidget=True):
        if forgetallwidget:
            self.forget_allwidget()
        for widget in widgets:
            widget.pack()
    def create_entry(self, width, text):
        pole = tk.Entry(self.root, width=width)
        pole.insert(0, text)
        pole.bind("<FocusIn>", lambda args: pole.delete('0', 'end') if pole.get() == text else None)
        pole.bind("<FocusOut>", lambda args: pole.insert(0, text) if not pole.get() else None)
        return pole
class Menu:
    def __init__(self):
        self.gui = GUI_function(root)
        pass
    def kontakty(self):
        gui.forget_allwidget()
        func.wyswietl_kontakty()
        pass
    def dodawania_kontaktow(self):
        cofnij_button = tk.Button(root,text="cofnij",command=self.Zalogowanych)
        self.gui.pack_widgets([Nowy_kontakt_pole,Nowy_kontakt_nazwa_pole,Nowy_kontakt_button,cofnij_button])
    def glowne(self):
        if email_pole_logowanie.get() != "Email":
            email_pole_logowanie.delete(0, END)
            email_pole_logowanie.insert(0, "")
        if passw_pole.get() != "Hasło" :
            passw_pole.delete(0, END)
            passw_pole.insert(0, "")
        self.gui.pack_widgets([Logowanie_butt, Menu_tworzenie_konta_butt, Menu_zapytania_button])
    def login_pack(self):
        cofnij = tk.Button(root, text="cofnij", command=self.glowne)
        self.gui.pack_widgets([email_pole_logowanie, passw_pole,zaloguj_button,cofnij])
    def zapytania(self):
        self.gui.pack_widgets([Zapytanie_A_button, Zapytanie_B_button, Zapytanie_C2_button, Zapytanie_C1_button,Zapytanie_imie_pole,Zapytanie_nazwisko_pole,Zapytanie_output])

        if email_nick:
            cofnij_button = tk.Button(root,text="cofnij",command=self.Zalogowanych)

        else:
            cofnij_button = tk.Button(root,text="cofnij",command=self.glowne)
        self.gui.pack_widgets([cofnij_button],None)
    def tworzenie_konta(self):
        cofnij = tk.Button(root, text="cofnij", command=self.glowne)
        self.gui.pack_widgets([email_pole, passw_pole,r1,r2, imie_pole, Nazwisko_pole, Data_urodzenia_pole, telefon_pole, stworz_konto_button,cofnij])
    def Zalogowanych(self):
        wyloguj = tk.Button(root, text="wyloguj", command=self.glowne)
        self.gui.pack_widgets([Lista_kontaktow_button,Dodaj_kontakt_button,Lista_wpisow_button,Menu_zapytania_button,wyloguj])
    def wpisy(self):
        func.wyswietl_wpisy()
        cofnij_button = tk.Button(root, text="cofnij", command=self.Zalogowanych)
        self.gui.pack_widgets([listbox,Menu_nowy_wpis_button,Nowy_edytuj_wpis_butt_2,Nowy_delete_wpis,cofnij_button])
        return
    def nowy_wpis(self):
        cofnij_button = tk.Button(root, text="cofnij", command=self.wpisy)
        self.gui.pack_widgets([Nowy_wpis_pole,Nowy_dodaj_wpis,cofnij_button])
    def edytuj_wpis(self):
        cofnij_button = tk.Button(root, text="cofnij", command=self.wpisy)
        self.gui.pack_widgets([Nowy_edytuj_wpis_pole,Nowy_edytuj_wpis_butt,cofnij_button])
    def zapytania_onlick(self):
        self.zapytania()
class on_enter:
    def key(event):#Enter robi to samo co myszka
        try:
            widget_with_focus = root.focus_get()
            widget_with_focus.invoke()
        except:
            return
    def imie_plec(event):#Autouzupełnia imie 
        male_names = ['Adam', 'Bartek', 'Cezary', 'Dawid', 'Edward']
        female_names = ['Anna', 'Beata', 'Celina', 'Dorota', 'Ewa']

        input_text = imie_pole.get().lower()
        if var.get() == 1:
            for name in female_names:
                if name.lower().startswith(input_text):
                    imie_pole.delete(0, 'end')
                    imie_pole.insert(0, name)
                    break
        elif var.get() == 2:
            for name in male_names:
                if name.lower().startswith(input_text):
                    imie_pole.delete(0, 'end')
                    imie_pole.insert(0, name)
                    break   
    def email(event):#Autouzupełnia email
        #pobieranie emailów
        query = f"SELECT email FROM `uzytkownicy`"
        cursor.execute(query)
        result = cursor.fetchall()
        input_text = email_pole_logowanie.get().lower()
        for emails in result:
            if emails[0].lower().startswith(input_text):
                email_pole_logowanie.delete(0, 'end')
                email_pole_logowanie.insert(0, emails[0])
                break
    def imie(event):#Autouzupełnia email
        #pobieranie emailów
        query = f"SELECT Imie FROM `dane_osoby`"
        cursor.execute(query)
        result = cursor.fetchall()
        input_text = Zapytanie_imie_pole.get().lower()
        for emails in result:
            if emails[0].lower().startswith(input_text):
                Zapytanie_imie_pole.delete(0, 'end')
                Zapytanie_imie_pole.insert(0, emails[0])
                break
    def nazwisko(event):#Autouzupełnia email
        #pobieranie emailów
        query = f"SELECT Nazwisko FROM `dane_osoby`"
        cursor.execute(query)
        result = cursor.fetchall()
        input_text = Zapytanie_nazwisko_pole.get().lower()
        for emails in result:
            if emails[0].lower().startswith(input_text):
                Zapytanie_nazwisko_pole.delete(0, 'end')
                Zapytanie_nazwisko_pole.insert(0, emails[0])
                break
class funkcja:
    def __init__(self):
        self.email_nick = email_nick
        self.select = (0,)
    def logowanie(self):
        
        
        def login(email, password): 
            password = passw_pole.get() + "sol"
            hash_password =  sha256(password.encode()).hexdigest() 
            query = f"SELECT uzytkownik_id FROM `uzytkownicy` WHERE email = %s AND hasło = %s"
            cursor.execute(query, (email, hash_password))
            result = cursor.fetchone()
            if result:
                global uzytkownik_id   
                uzytkownik_id = result[0]
                return True
            else:
                return False

        def try_login():
            email = email_pole_logowanie.get()
            password = passw_pole.get()
            if login(email, password) == True:
                zaloguj_button.pack_forget()
                
                menu.Zalogowanych()
                global email_nick
                email_nick = email
        global zaloguj_button
        zaloguj_button = tk.Button(root,text="Zaloguj",command=try_login)
        menu.login_pack()
    def stworz_konto(self):
        
        
        query2 = "INSERT INTO `uzytkownicy` (`email`, `Hasło`,`Imie`, `Nazwisko`, `Data_urodzenia`, `telefon`) VALUES (%s, %s, %s, %s, %s, %s)"
        password = passw_pole.get() + "sol"
        hash_password =  sha256(password.encode()).hexdigest()
        email = email_pole.get()
        numer = telefon_pole.get()
        if not "@" in email: 
            messagebox.showerror("Error","Email nie zawiera @")
            return
        if not len(str(numer)) == 9:
            messagebox.showerror("Error","Telefon nie ma 9 znaków")
            return
        try:
            cursor.execute(query2,(email_pole.get(),hash_password,imie_pole.get(),Nazwisko_pole.get(),Data_urodzenia_pole.get(),telefon_pole.get()))
            mydb.commit()
        except:
            messagebox.showerror("Error","Konto nie mogło zostać utworzone")
        else:
            global email_nick
            email_nick = email_pole.get()
            menu.Zalogowanych()


    def wyswietl_kontakty(self):
        def odswiez_kontakty():
            # Usuń wszystkie istniejące wiersze
            for i in tree.get_children():
                tree.delete(i)

            # Ponownie wykonaj zapytanie
            cursor.execute(query, (email_nick,))
            result = cursor.fetchall()

            # Wypełnij drzewo nowymi danymi
            for i, row in enumerate(result):
                tree.insert("", i, values=(row[0], row[1], row[2],row[3]))


        query = ("SELECT k.Nazwa,ku.email ,ku.imie,ku.nazwisko,ku.Data_urodzenia,ku.telefon FROM kontakty k "
                "LEFT JOIN uzytkownicy u on k.uzytkownik_ID = u.Uzytkownik_ID "
                "LEFT JOIN uzytkownicy ku on k.kontakt_ID = ku.Uzytkownik_ID "
                "WHERE u.email = %s")
        cursor.execute(query, (email_nick,))
        result = cursor.fetchall()
        # Tworzenie tabeli
        tree = ttk.Treeview(root, show='headings')
        tree["columns"] = ("Nazwa","Email", "Imię", "Nazwisko")
        tree.column("Nazwa")
        tree.column("Email")
        tree.column("Imię")
        tree.column("Nazwisko")
        tree.heading("Email", text="Email")
        tree.heading("Imię", text="Imię")
        tree.heading("Nazwisko", text="Nazwisko")

        # Wypełnianie tabeli danymi
        for i, row in enumerate(result):
            tree.insert("", i, values=(row[0], row[1], row[2],row[3]))

        # Obsługa kliknięcia na wiersz
        info_box = tk.Entry(root,width=120 ,state='readonly',justify='center')
        info_box.pack()
        #Podczas podwójnego klikniecia 
        def on_click(event):
            item = tree.selection()[0]
            values = tree.item(item,"values")
            for row in result:
                if row[0] == values[0]:
                    info = f"Data urodzenia: {row[3]}, Telefon: {row[4]}"
                    info_box.config(state='normal')
                    info_box.delete(0, 'end')
                    info_box.insert(0, info)
                    info_box.config(state='readonly')

        tree.bind("<Double-1>", on_click)
        #Tworzenie przycisków
        odswiez_button = tk.Button(root, text="Odśwież", command=odswiez_kontakty)
        cofnij_button = tk.Button(root, text="cofnij", command=menu.Zalogowanych)

        tree.pack()    
        odswiez_button.pack()
        cofnij_button.pack() 
    def nowykontakt(self):
        #Sprawdza czy dodajesz sam siebie
        if Nowy_kontakt_pole.get() == email_nick:
            messagebox.showerror("Error","Nie możesz dodać sam siebie")
            return
        
        q_kontakt_id,q_uzytkownika_id = f"select u.uzytkownik_ID from uzytkownicy u WHERE u.email = '{Nowy_kontakt_pole.get()}'",f"select u.uzytkownik_ID from uzytkownicy u WHERE u.email = '{email_nick}'"

        cursor.execute(q_kontakt_id)
        result_kontakt = cursor.fetchone()
        cursor.execute(q_uzytkownika_id)
        result_uzytkownik = cursor.fetchone()

        #Sprawdza czy kontakt już istnieje
        check_query = f"SELECT * FROM `kontakty` WHERE uzytkownik_ID = {result_uzytkownik[0]} AND kontakt_ID = {result_kontakt[0]}"
        cursor.execute(check_query)
        check_result = cursor.fetchone()
        if check_result:
            messagebox.showerror("Error","Ten kontakt już istnieje")
            return
        #Wpisuje kontakt
        nazwa_kontaktu = Nowy_kontakt_nazwa_pole.get()
        query = f"INSERT INTO `kontakty` (uzytkownik_ID,kontakt_ID,nazwa) VALUES ({result_uzytkownik[0]},{result_kontakt[0]},'{nazwa_kontaktu}')"
        cursor.execute(query)
        mydb.commit()
    def nowywpis(self):
        query = "INSERT INTO wpisy (Tworca_id, wpis) VALUES (%s, %s)"
        cursor.execute(query, (uzytkownik_id, Nowy_wpis_pole.get()))
        mydb.commit()
        menu.wpisy()
    def usuwanie_wpisu(self):
        selected = listbox.curselection()
        if selected:
            content = listbox.get(selected)
            account_id = int(content.split('-')[1].split(':')[0].strip())
            if account_id == uzytkownik_id:
                wpis_id = int(content.split('-')[0].strip())
                query = "DELETE FROM wpisy WHERE Tworca_id = %s AND wpis_id = %s"
                cursor.execute(query, (account_id, wpis_id))
                mydb.commit()
                menu.wpisy()
            else:
                messagebox.showwarning("Permission Denied", "Nie masz uprawnień do usunięcia tego wpisu")
        else:
            messagebox.showwarning("Error 420", "Nie wybrałeś żadnego wpisu")
    def edytowanie_wpisu(self):
        selected = listbox.curselection()
        self.select = selected
        if selected:
            content = listbox.get(selected)
            account_id = int(content.split('-')[1].split(':')[0].strip())
            
            if account_id == uzytkownik_id:
                menu.edytuj_wpis()
            else:
                messagebox.showwarning("Permission Denied", "Nie masz uprawnień do edytowania tego wpisu")
        else:
            messagebox.showwarning("Error 420", "Nie wybrałeś żadnego wpisu")
    def edytowanie_wpisu_właściwe(self):
        content = listbox.get(self.select)
        account_id = int(content.split('-')[1].split(':')[0].strip())
        wpis_id = int(content.split('-')[0].strip())
        nowa_tresc = Nowy_edytuj_wpis_pole.get()
        query = "UPDATE wpisy SET wpis = %s WHERE Tworca_id = %s AND wpis_id = %s"
        cursor.execute(query, (nowa_tresc,account_id, wpis_id))
        mydb.commit()
        menu.wpisy()    
    def wyswietl_wpisy(self):
        query = f"SELECT u.imie,u.nazwisko,w.wpis,w.tworca_id,w.wpis_id  FROM wpisy w LEFT JOIN uzytkownicy u on u.Uzytkownik_id = w.tworca_id GROUP BY w.wpis_id"
        cursor.execute(query)
        result = cursor.fetchall()
        global listbox
        listbox = Listbox(root,width=100)
        for row in result:
            listbox.insert(END, f"{row[4]}-{row[3]}:{row[0] + ' '}{row[1]},Wpis: {row[2]}")
class zapytanie:
    def A():
        Zapytanie_A_komenda="SELECT do.imie, do.nazwisko, COUNT(*) AS liczba_wnukow FROM osoba o JOIN dane_osoby do ON o.Id = do.Dane_ID JOIN rodzic r ON o.Id = r.rodzic_id JOIN rodzic r2 ON r.dziecko_id = r2.rodzic_id GROUP BY do.imie, do.nazwisko ORDER BY liczba_wnukow DESC LIMIT 1;"
        cursor.execute(Zapytanie_A_komenda)
        result = cursor.fetchone()
        Zapytanie_output.config(state='normal')  # Włącz pole tekstowe
        Zapytanie_output.delete("1.0", 'end')  # Usuń poprzedni tekst
        Zapytanie_output.insert('1.0', result)  # Wstaw nowy tekst
        Zapytanie_output.config(state='disabled')  # Wyłącz pole tekstowe
    def B():
        Zapytanie_B_komenda="SET @wszyscy =(SELECT COUNT(*) FROM praca); SELECT CONCAT(t.Nazwa, ' ', CONVERT((COUNT(p.Pracownik_ID) / @wszyscy * 100), UNSIGNED), '%') as procent_zatrudnienia FROM praca p JOIN firma f ON f.ID = p.Firma_ID JOIN typ_pracy t on p.Typ_pracy_id = t.Typ_pracy_id GROUP BY t.Nazwa;"
        for result in cursor.execute(Zapytanie_B_komenda, multi=True):
            pass
        results = cursor.fetchall()
        Zapytanie_output.config(state='normal')  # Włącz pole tekstowe
        Zapytanie_output.delete("1.0", 'end')  # Usuń poprzedni tekst
        for result in results:
            Zapytanie_output.insert('end', result[0] + '\n')  # Wstaw nowy tekst
        Zapytanie_output.config(state='disabled')  # Wyłącz pole tekstowe
    def C2():
        Zapytanie_C_komenda_a = """SELECT da.Imie, 
        convert((SELECT COALESCE(SUM(pr.Zarobki),0) FROM praca pr WHERE om.ID = pr.Pracownik_ID) + SUM(p.Zarobki)  +
        (SELECT COALESCE(SUM(p1.Zarobki),0) FROM praca p1 WHERE o1.ID = p1.Pracownik_ID) +
        (SELECT COALESCE(SUM(pm1.Zarobki),0) FROM praca pm1 WHERE om1.ID = pm1.Pracownik_ID),UNSIGNED) as Zarobki_rodziny
        FROM praca p
        LEFT JOIN osoba o ON o.ID = p.Pracownik_ID 
        LEFT JOIN dane_osoby da ON da.Dane_ID = o.ID
        LEFT JOIN osoba om ON om.ID = o.Malzonek_ID
        LEFT JOIN rodzic r1 ON r1.Rodzic_ID = o.ID
        LEFT JOIN osoba o1 ON o1.ID = r1.Dziecko_ID
        LEFT JOIN osoba om1 ON om1.ID = o1.Malzonek_ID """
        a,b = 0,0
        Zapytanie_C_komenda_b_1,Zapytanie_C_komenda_b_2 = '',''
        imie = Zapytanie_imie_pole.get()
        nazwisko = Zapytanie_nazwisko_pole.get()
        imie_nazwisko = ()
        if imie != "Imie" and imie:
            Zapytanie_C_komenda_b_1 = "WHERE da.Imie = %s"
            a = 1
            imie_nazwisko += (imie,)

        if nazwisko != "Nazwisko" and nazwisko:
            Zapytanie_C_komenda_b_2 = "da.Nazwisko = %s"
            if a == 0:  # if Zapytanie_C_komenda_b_1 is not set, add WHERE clause
                Zapytanie_C_komenda_b_2 = "WHERE " + Zapytanie_C_komenda_b_2
            b = 1
            imie_nazwisko += (nazwisko,)

        if a and b:
            Zapytanie_C_komenda_b_1 = Zapytanie_C_komenda_b_1 + " and "

        Zapytanie_C_komenda_b = Zapytanie_C_komenda_b_1 + Zapytanie_C_komenda_b_2
        Zapytanie_c_komenda_c ="""
        GROUP BY p.Pracownik_ID
        ORDER BY 2
        LIMIT 1
        """
        Zapytanie_C_komenda = Zapytanie_C_komenda_a + Zapytanie_C_komenda_b + Zapytanie_c_komenda_c
        cursor.execute(Zapytanie_C_komenda, imie_nazwisko)
        result = cursor.fetchall()
        

        Zapytanie_output.config(state='normal')  # Włącz pole tekstowe
        Zapytanie_output.delete("1.0", 'end')  # Usuń poprzedni tekst
        Zapytanie_output.insert('1.0', result[0])  # Wstaw nowy tekst
        Zapytanie_output.config(state='disabled')  # Wyłącz pole tekstowe
    def C1():
        Zapytanie_C_komenda_a = """SELECT da.Imie,
        CAST((SELECT COALESCE(SUM(pr.Zarobki),0) FROM praca pr WHERE om.ID = pr.Pracownik_ID) + SUM(p.Zarobki) AS UNSIGNED ) as Zarobki_rodziny
        FROM praca p
        LEFT JOIN osoba o ON o.ID = p.Pracownik_ID
        LEFT JOIN dane_osoby da ON da.Dane_ID = o.ID
        LEFT JOIN osoba om ON om.ID = o.Malzonek_ID """
        a,b = 0,0
        Zapytanie_C_komenda_b_1,Zapytanie_C_komenda_b_2 = '',''
        imie = Zapytanie_imie_pole.get()
        nazwisko = Zapytanie_nazwisko_pole.get()
        imie_nazwisko = ()
        if imie != "Imie" and imie:
            Zapytanie_C_komenda_b_1 = "WHERE da.Imie = %s"
            a = 1
            imie_nazwisko += (imie,)

        if nazwisko != "Nazwisko" and nazwisko:
            Zapytanie_C_komenda_b_2 = "da.Nazwisko = %s"
            if a == 0:  # if Zapytanie_C_komenda_b_1 is not set, add WHERE clause
                Zapytanie_C_komenda_b_2 = "WHERE " + Zapytanie_C_komenda_b_2
            b = 1
            imie_nazwisko += (nazwisko,)

        if a and b:
            Zapytanie_C_komenda_b_1 = Zapytanie_C_komenda_b_1 + " and "

        Zapytanie_C_komenda_b = Zapytanie_C_komenda_b_1 + Zapytanie_C_komenda_b_2
        Zapytanie_c_komenda_c ="""
        GROUP BY p.Pracownik_ID
        ORDER BY 2
        LIMIT 1
        """
        Zapytanie_C_komenda = Zapytanie_C_komenda_a + Zapytanie_C_komenda_b + Zapytanie_c_komenda_c
        cursor.execute(Zapytanie_C_komenda, imie_nazwisko)
        result = cursor.fetchall()
        Zapytanie_output.config(state='normal')  # Włącz pole tekstowe
        Zapytanie_output.delete("1.0", 'end')  # Usuń poprzedni tekst
        Zapytanie_output.insert('1.0', result[0])  # Wstaw nowy tekst
        Zapytanie_output.config(state='disabled')  # Wyłącz pole tekstowe

menu = Menu()
gui = GUI_function(root)
func = funkcja()

#kontakty
Lista_kontaktow_button = tk.Button(root,width=60,text="Lista kontaktow",command=menu.kontakty)
Lista_wpisow_button = tk.Button(root,width=60,text="Lista wpisow",command=menu.wpisy)
Dodaj_kontakt_button = tk.Button(root,width=60,text="Dodaj nowy kontakt",command=menu.dodawania_kontaktow)

#Nowy kontakt
Nowy_kontakt_pole = gui.create_entry(60, "Email kontaktu")
Nowy_kontakt_nazwa_pole = gui.create_entry(60, "Nazwa kontaktu")
Nowy_kontakt_button = tk.Button(root,text="Dodaj",command=func.nowykontakt)

#wpisy
Nowy_wpis_pole = gui.create_entry(60, "Wpis")
Nowy_edytuj_wpis_pole = gui.create_entry(60, "Wpis")

Nowy_dodaj_wpis = tk.Button(root,text="Dodaj wpis",command=func.nowywpis)
Nowy_delete_wpis = tk.Button(root, text="Usuń wpis", command=func.usuwanie_wpisu)
Nowy_edytuj_wpis_butt = tk.Button(root, text="Edytuj wpis wew", command=func.edytowanie_wpisu_właściwe)
Menu_nowy_wpis_button = tk.Button(root,text="Dodaj",command=menu.nowy_wpis)


Nowy_edytuj_wpis_butt_2 = tk.Button(root, text="Edytuj wpis", command=func.edytowanie_wpisu)
#Menu logowania
email_pole_logowanie = gui.create_entry(60, "Email")
passw_pole = gui.create_entry(60, "Hasło")
email_pole_logowanie.bind('<Return>', on_enter.email)

#Menu tworzenia konta
email_pole = gui.create_entry(60, "Email")
var = tk.IntVar(value=0)
r1 = tk.Radiobutton(root, text='K', variable=var, value=1)
r2 = tk.Radiobutton(root, text='M', variable=var, value=2)
Nazwisko_pole = gui.create_entry(60, "Nazwisko")
Data_urodzenia_pole = DateEntry(root,width=57, year=2021, month=6, day=22, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
telefon_pole = gui.create_entry(60, "Numer telefonu")
stworz_konto_button = tk.Button(root,text="Stwórz konto",command=func.stworz_konto)
imie_pole = gui.create_entry(60, "Imie")
imie_pole.bind('<Return>', on_enter.imie_plec)
root.bind('<Return>', on_enter.key)

#Menu główne
Logowanie_butt = tk.Button(root, width=30,text="Logowanie",command=func.logowanie)
Menu_tworzenie_konta_butt = tk.Button(root,text="Tworzenie konta", width=30,command=menu.tworzenie_konta)
Menu_zapytania_button = tk.Button(root,text="Zapytania jako konto anonimowe", width=30,command=menu.zapytania_onlick)

#Zapytania #zrobić funkcje zapytania i gui do tego
Zapytanie_A_button = tk.Button(root,text="Znajdź imię i nazwisko osoby posiadającej największą liczbę wnucząt", width=60,command=zapytanie.A)
Zapytanie_B_button = tk.Button(root,text="Znajdź procent zatrudnionych na etacie i na zlecenie", width=60,command=zapytanie.B)
Zapytanie_C2_button = tk.Button(root,text="Znajdź rodzinę najmniej zarabiającą.2 pokolenia", width=60,command=zapytanie.C2)
Zapytanie_C1_button = tk.Button(root,text="Znajdź rodzinę najmniej zarabiającą.1 pokolenie", width=60,command=zapytanie.C1)
Zapytanie_output = tk.Text(root, state='disabled')
Zapytanie_imie_pole = gui.create_entry(60 , "Imie")
Zapytanie_imie_pole.bind('<Return>', on_enter.imie)
Zapytanie_nazwisko_pole = gui.create_entry(60 , "Nazwisko")
Zapytanie_nazwisko_pole.bind('<Return>', on_enter.nazwisko)


if __name__ == "__main__":
    menu.glowne()
    root.mainloop()





