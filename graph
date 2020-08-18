import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

URL = 'https://www.basketball-reference.com/players/i/irvinky01.html' # To set the URL I'm retrieving the data from
response = requests.get(URL) # To import the URL
soup = BeautifulSoup(response.content, 'html.parser')

columns = ['Age', 'Tm', 'Lg', 'Pos', 'G', 'GS', 'MP', 'FG', 'FGA',
           'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT',
           'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK',
           'TOV', 'PF', 'PTS']
df = pd.DataFrame(columns=columns)

table = soup.find('table', attrs={'class':'row_summable'}).tbody
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(row, index=columns), ignore_index=True)

df.to_csv('Kyrie Irving Stats.csv', index=False)

df = pd.read_csv('Kyrie Irving Stats.csv')

%matplotlib inline

Age_list = list(df.Age.unique())
print(Age_list)

plt.plot(df.Age.unique), label
plt.legend('Kyrie Irving Points per Game by Age')
plt.xlabel('Age')
plt.ylabel('Points per Game')
plt.show()
