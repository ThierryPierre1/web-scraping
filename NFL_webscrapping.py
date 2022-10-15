import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.nfl.com/standings/league/2022/REG')

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())

NFL = soup.find('table',class_='d3-o-table')
print(NFL)
output_NFL = []

for teams in NFL:
    print(NFL.text)
    data = NFL.text

Team_info = soup.find('div', class_='d3-o-club-fullname')
print(Team_info)
output_Team_info = []
for Team_info in NFL:
    print(Team_info.text)
    info = Team_info.text
len(Team_info)

Record = soup.find_all('th',scope= 'col', class_='header')
print(Record)
output_Record = []
for Record in NFL:
    print(Record.text)
    wins_loses = Record.text
len(wins_loses)
len(Record)

list1 = Team_info
list2 = Record

dictionary = {'name': list1, 'record': list2}

df = pd.DataFrame({'name':[info], 'record':[wins_loses]})
df

df.to_csv('/Users/thierrypierre/Desktop/NFL_Standings.csv')
