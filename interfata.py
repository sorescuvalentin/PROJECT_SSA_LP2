import webbrowser
from functools import partial
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import reload

f = open("dateExtrase.txt", "r", encoding='utf-8')

dictionar = {"bla": "bla"}
dictionar.popitem()

def PrinteazaSosire(labelSosire:Label,textStatie):
    labelSosire.config(text="Urmatoarea sosire la " + textStatie + " : " +dictionar.get(textStatie))

def GenereazaSosiri(linieTroleu, tab) :
    dictionar.clear()
    linia_curenta = f.readline()
    while linia_curenta.find(linieTroleu) == -1:
        linia_curenta = f.readline()
    Label(tab, text=linia_curenta.rstrip()).pack()
    labelSosire=Label(tab, text="APASATI UN BUTON PENTRU URMATOAREA SOSIRE")
    labelSosire.pack()
    linia_curenta = f.readline()
    while linia_curenta.find(linieTroleu) == -1:
        if linia_curenta.find("Sta") == -1 and linia_curenta.find("Sosire") == -1:
            if linia_curenta[0].isalpha():
                textStatie=linia_curenta
                textStatie=textStatie.rstrip()
                Button(tab,text=textStatie,command=partial(PrinteazaSosire,labelSosire,textStatie)).pack(side='top')

                linia_curenta=f.readline()
                if linia_curenta[0].isnumeric():
                    textSosire=linia_curenta
                    textSosire=textSosire.rstrip()
                    dictionar[textStatie]=textSosire
        linia_curenta = f.readline()
    f.seek(0, 0)

window = Tk()
window.title('Project LP2 - RATT TIMISOARA')
window.geometry('900x600')
#Style
style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn')

#Tabs
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)
tab7 = ttk.Frame(tab_control)
tab8 = ttk.Frame(tab_control)
tab9 = ttk.Frame(tab_control)
tab10 = ttk.Frame(tab_control)

tab_control.add(tab1, text=f'{"Acasa":^20}')
tab_control.add(tab10, text=f'{"Despre noi":^20}')
tab_control.add(tab2, text=f'{"Linia 11":^20}')
tab_control.add(tab3, text=f'{"Linia M11":^20}')
tab_control.add(tab4, text=f'{"Linia 14":^20}')
tab_control.add(tab5, text=f'{"Linia M14":^20}')
tab_control.add(tab6, text=f'{"Linia 15":^20}')
tab_control.add(tab7, text=f'{"Linia 16":^20}')
tab_control.add(tab8, text=f'{"Linia 17":^20}')
tab_control.add(tab9, text=f'{"Linia 18":^20}')

#Acasa
cover = ImageTk.PhotoImage(Image.open("logo.jpg"))
Label(tab1,image=cover).pack()
#Despre noi
logo = ImageTk.PhotoImage(Image.open("logo.png"))
Label(tab10,image=logo).pack()
Label(tab10,text='\n\nDespre aplicatie', font='Calibri, 16', bd='1').pack()
Label(tab10,text='\nTimpii afisati in formatul "x min", reprezinta timpi de asteptare reali, calculati pe baza pozitiei GPS a vehiculului. \n Ei pot varia chiar in sens crescator, atunci cand vehiculul are o viteza medie mai mica decat cea trimisa anterior \n datele se trimit la un interval de 30 sec. Timpii afisati in formatul hh:mm, reprezinta ora de sosire in statie \n conform graficului.  Fata de grafic pot aparea intarzieri de cateva minute, in functie de trafic.').pack()
Label(tab10,text='\n\nDezvoltatori aplicatie', font='Calibri, 12', bd='1').pack()
Label(tab10,text='\nSorescu Valentin - Extragere/Prelucrare date\nStankov Sasa - Interfata/Design\nElena Atomei - Interfata/Harta Live').pack()

#Linia11
url = 'linia11.html'
def linia11():
    webbrowser.open(url)
Button(tab2, text='DESCHIDE HARTA - LINIA 11', command=linia11).pack()
Button(tab2, text='REINCARCA LINIE', command=lambda:[reload.Executor(),GenereazaSosiri("Linia 11", tab2)]).pack()

#LiniaM11
url2 = 'liniaM11.html'
def liniaM11():
    webbrowser.open(url2)
Button(tab3, text='DESCHIDE HARTA - LINIA M11', command=liniaM11).pack()
Button(tab3, text='REINCARCA LINIE', command=lambda:[reload.Executor(),GenereazaSosiri("Linia M11", tab3)]).pack()

#Linia14
url3 = 'linia14.html'
def linia14():
    webbrowser.open(url3)
Button(tab4, text='DESCHIDE HARTA - LINIA 14', command=linia14).pack()
Button(tab4, text='REINCARCA LINIE', command=lambda:[reload.Executor(),GenereazaSosiri("Linia 14", tab4)]).pack()

#LiniaM14
url4 = 'liniaM14.html'
def liniaM14():
    webbrowser.open(url4)
Button(tab5, text='DESCHIDE HARTA - LINIA M14', command=liniaM14).pack()
Button(tab5, text='REINCARCA LINIE', command=lambda:[reload.Executor(),GenereazaSosiri("Linia M14", tab5)]).pack()

#Linia15
url5 = 'linia15.html'
def linia15():
    webbrowser.open(url5)
Button(tab6, text='DESCHIDE HARTA - LINIA 15', command=linia15).pack()
Button(tab6, text='REINCARCA LINIE', command=lambda:[reload.Executor(),GenereazaSosiri("Linia 15", tab6)]).pack()

#Linia16
url6 = 'linia16.html'
def linia16():
    webbrowser.open(url6)
Button(tab7, text='DESCHIDE HARTA - LINIA 16', command=linia16).pack()
Button(tab7, text='REINCARCA LINIE', command=lambda:[reload.Executor(),GenereazaSosiri("Linia 16", tab7)]).pack()

#Linia17
url7 = 'linia17.html'
def linia17():
    webbrowser.open(url7)
Button(tab8, text='DESCHIDE HARTA - LINIA 17', command=linia17).pack()
Button(tab8, text='REINCARCA LINIE', command=lambda:[reload.Executor(),GenereazaSosiri("Linia 17", tab8)]).pack()

#Linia18
url8 = 'linia18.html'
def linia18():
    webbrowser.open(url8)
Button(tab9, text='DESCHIDE HARTA - LINIA 18', command=linia18).pack()
Button(tab9, text='REINCARCA LINIE', command=lambda:[reload.Executor(),GenereazaSosiri("Linia 18", tab9)]).pack()


tab_control.pack(expand=1,fill='both')

window.mainloop()