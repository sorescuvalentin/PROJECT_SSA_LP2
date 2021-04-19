from bs4 import BeautifulSoup
import requests

url = "http://86.125.113.218:61978/html/timpi/trasee.php?param1=1106"
page = requests.get(url)
pagetext = page.text

pricetable = {
    "Sosire" : [],
}
print(pricetable)
soup = BeautifulSoup(pagetext, 'html.parser')

with open ('NiftyList.txt', 'w', encoding="utf-8") as f:

    for row in soup.find_all('tr'):
        for col in row.find_all('td'):
            f.write(col.text + '\n')