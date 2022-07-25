import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.ticker as tck


class Content:
    def __init__(self, url, bb_player_name, stats):
        self.url = url
        self.player_name = bb_player_name
        self.stats = stats


def get_page(url):
    # Imports the URL
    data = requests.get(url).text
    # Scrapes the content of the page
    return BeautifulSoup(data, 'html.parser')


def scrape_nba_data(url):
    soup = get_page(url)
    headers = soup.find('table', attrs={'id': 'per_game'}).thead
    column_trs = headers.find_all('tr')

    # Retrieves column names from website
    for tr in column_trs:
        td = tr.find_all('th') + tr.find_all('td')
        columns = [i.text for i in td]
        del columns[0]
        df = pd.DataFrame(columns=columns)

        # Retrieves player stats from website
        table = soup.find('table', attrs={'id': 'per_game'}).tbody
        body_trs = table.find_all('tr')
        for body_tr in body_trs:
            tds = body_tr.find_all('td')
            row = [td.text.replace('\n', '') for td in tds]
            df = df.append(pd.Series(row, index=columns), ignore_index=True)

        # Retrieves player name from website
        player_html = soup.findAll('h1')

        for player in player_html:
            player_text = player.find_all('span')
            player_name = [i.text for i in player_text][0]

            return Content(url, player_name, df)


'''
x = np.arange(19, 30)
fig, ax = plt.subplots()
colors = {'CLE': 'maroon', 'BOS': 'tab:green', 'BRK': 'k'}
plt.bar(df['Age'], df['PTS'], color=df['Tm'].map(colors))
plt.title('Kyrie Irving Points per Game by Age')
plt.xlabel('Age')
plt.xticks(x)
plt.ylabel('Points per Game')
plt.ylim([18, 28])
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.show()

df2 = df[['Age', 'PTS']].copy()

test_size = 9

train, test = df2.iloc[:test_size], df2.iloc[test_size:]

fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.plot(train['Age'], train['PTS'])
ax.plot(test['Age'], test['PTS'])
plt.show()

from pmdarima.arima import auto_arima

model = auto_arima(train['PTS'], start_p=1, start_q=1, test = 'adf', max_p=1, max_q=1, seasonal=False, stepwise=True)

print(model.summary())

prediction, confint = model.predict(n_periods=test_size, return_conf_int=True)
print(prediction)

cf = pd.DataFrame(confint)
print(cf)
prediction_series = pd.Series(prediction,index=test.index)
fig, ax = plt.subplots(1, 1, figsize=(15, 5))
ax.plot(df2['PTS'])
ax.plot(prediction_series)
ax.fill_between(prediction_series.index,
                cf[0],
                cf[1],color='grey',alpha=.3)
plt.show()
'''

# testing
'''
table = get_page('https://www.basketball-reference.com/players/i/irvinky01.html').find("table", { "id" : "per_game" })
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('th') + tr.find_all('td')
    row = [i.text for i in td]
    print(row)'''
