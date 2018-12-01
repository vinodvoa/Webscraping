import requests

from bs4 import BeautifulSoup
from openpyxl import Workbook

URL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

page = requests.get(URL)

soup = BeautifulSoup(page.content)
# print(soup.body)

table = soup.find('table', {'class': 'wikitable sortable'})
# print(table)

wb = Workbook()
ws = wb.active
i = 1

for row in table.find_all('tr')[1:]:
    ticker = row.find_all('td')[0].text
    company = row.find_all('td')[1].text
    # print(ticker, company)
    ws['A' + str(i)] = ticker
    ws['B' + str(i)] = company
    i += 1

wb.save('sp500.xlsx')
