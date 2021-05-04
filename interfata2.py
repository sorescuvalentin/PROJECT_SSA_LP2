
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Project LP2 - RATT TIMISOARA')
window.geometry('700x500')
#Style
style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn')

#Tabs
tab_control = ttk.Notebook(window,style='lefttab.TNotebook')
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

#Labels
label1 = Label(tab1,text='Hei',padx=5,pady=5)


tab_control.pack(expand=1,fill='both')


window.mainloop()