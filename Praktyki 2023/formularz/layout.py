
import PySimpleGUI as sg
def layout(pan,woj,powa):
    sg.theme('DarkAmber')
    sg.Text('Imie              ',size=(15, 1)), sg.InputText()
    layout = [  
            [sg.Text('Imie              ',size=(15, 1)), sg.InputText(key="input_imie")],
            [sg.Text('Nazwisko          ',size=(15, 1)), sg.InputText(key="input_nazwisko")],
            [sg.Text('Ulica             ',size=(15, 1)), sg.InputText(key="input_ulica")],
            [sg.Text('Nr domu           ',size=(15, 1)), sg.InputText(key="input_nrdomu")],
            [sg.Text('Miejscowosc       ',size=(15, 1)), sg.InputText(key="input_miejscowosc")],
            [sg.Text('Kod pocztowy      ',size=(15, 1)), sg.InputText(key="input_kod")],
            [sg.Text('Telefon           ',size=(15, 1)), sg.InputText(key="input_telefon")],
            [sg.Text('Email             ',size=(15, 1)), sg.InputText(key="input_email")],
            [sg.Text('Zawod             ',size=(15, 1)), sg.InputText(key="input_zawod")],
            [sg.Text('PESEL             ',size=(15, 1),key="lpesel"), sg.InputText(key="input_pesel")],
            [sg.Text('Miejsce urodzenia ',size=(15, 1),), sg.InputText(key="input_miejsce")],
            [sg.Text('wiek*             ',size=(15, 1)), sg.InputText(key="input_wiek")],
            [sg.Text('plec*             ',size=(15, 1)), sg.InputText(key="input_plec")],
            [sg.Text('Panstwo             ',size=(15, 1)),sg.Combo(values=pan,key='input_kraj',enable_events=True,default_value=' ',readonly=True)],
            [sg.Text('Wojewodztwo             ',size=(15, 1)),sg.Combo(values=woj[0],enable_events=True,visible=False,key='input_woj',default_value=' ',readonly=True)],
            [sg.Text('Powiat',size=(15, 1)),sg.Combo(values=powa[0],visible=False,enable_events=True,key='input_pow',default_value=' ',readonly=True)],

            [sg.Button('Wyslij'),sg.Button('Clear',),sg.Button('Popraw')]]
            #[sg.Button('Sprawdz Wszystko'),sg.Button('Clear'),sg.Button('Zapisz do bazydanych'),sg.Button('Update'),sg.Button('Usun'),sg.Button('Usun2'),sg.Button('Data table'),sg.InputText("ID",key="input_id", size = (30,30) )]]
            #[sg.Text('wiek*             ',size=(15, 1)), sg.InputText(key="input_wiek"),sg.Button('Auto wiek')],
            #[sg.Text('plec*             ',size=(15, 1)), sg.InputText(key="input_plec"),sg.Button('Auto plec')],
            #[sg.Text('PESEL             ',size=(15, 1),key="lpesel"), sg.InputText(key="input_pesel"),sg.Button('Sprawdz pesel')],
    return layout