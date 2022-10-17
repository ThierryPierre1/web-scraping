import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.premierleague.com/tables')

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())

table = soup.find('tbody', class_='tableBodyContainer isPL')
print(table)

output_titles = []
for i in table:
    print(i.text)
    output_titles.append(i.text)

for teams in table:
    print(teams.text)
    data = table.text
    standings = data.strip() 
    record = standings.replace('\n','')
    plStandings = record.replace(' ','')
len(plStandings)

list1 = plStandings

dictionary = {'name': list1} 

df = pd.DataFrame({'name': [list1]})
df

df.to_csv('/Users/thierrypierre/Desktop/PremierLeague_standing')
