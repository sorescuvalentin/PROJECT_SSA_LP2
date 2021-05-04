from bs4 import BeautifulSoup
import requests
from tkinter import *

urls = ['http://86.125.113.218:61978/html/timpi/trasee.php?param1=990', 'http://86.125.113.218:61978/html/timpi/trasee.php?param1=2786', 'http://86.125.113.218:61978/html/timpi/trasee.php?param1=1006', 'http://86.125.113.218:61978/html/timpi/trasee.php?param1=2766', 'http://86.125.113.218:61978/html/timpi/trasee.php?param1=989', 'http://86.125.113.218:61978/html/timpi/trasee.php?param1=1206', 'http://86.125.113.218:61978/html/timpi/trasee.php?param1=1086', 'http://86.125.113.218:61978/html/timpi/trasee.php?param1=1166']

class Application(Frame):
    def __init__(self, master=None, on_reload=None):
        Frame.__init__(self, master)
        self.pack()
        self.my_reload = Button(self)
        self.my_reload["text"] = "Reload",
        self.my_reload["command"] = on_reload
        self.my_reload.pack()

        with open ('dateExtrase.txt', 'w', encoding="utf-8") as f:
            for url in urls:
                page = requests.get(url)
                html = page.text
                soup = BeautifulSoup(html, 'html.parser')
                for row in soup.find_all('tr'):
                    for col in row.find_all('td'):
                        f.write(col.text + '\n')

