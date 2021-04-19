from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'http://86.125.113.218:61978/html/timpi/trasee.php?param1=1106'

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
table_rows = soup.find_all('tr')
list1 = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    list1.append(row)

df=pd.DataFrame(list1)

df = df.iloc[0:22]
df.dropna(axis='columns', how='all', inplace=True)
print(df)