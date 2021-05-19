from bs4 import BeautifulSoup
import requests
from tkinter import *
from tqdm import tqdm

urls = 'http://86.125.113.218:61978/html/timpi/trol.php'
link_de_unit = ['http://86.125.113.218:61978/html/timpi/']

page = requests.get(urls)
html = page.text

class Application(Frame):
    def __init__(self, master=None, on_reload=None):
        Frame.__init__(self, master)
        self.pack()
        self.my_reload = Button(self)
        self.my_reload["command"] = on_reload
        self.my_reload.pack()

extragere_param = re.findall("(?<=')trasee.+?(?=')", html)
lista_finala = []
for i in tqdm(link_de_unit):
    for j in tqdm(extragere_param):
        lista_finala.append(i + j)


        with open ('dateExtrase.txt', 'w', encoding="utf-8") as f:
            for url in lista_finala:
                page = requests.get(url)
                html = page.text
                soup = BeautifulSoup(html, 'html.parser')
                for row in soup.find_all('tr'):
                    for col in row.find_all('td'):
                        f.write(col.text + '\n')


