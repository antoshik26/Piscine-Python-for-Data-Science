import sys
import time
from bs4 import BeautifulSoup
import requests
import ssl


def get_row(ticker, row):
	ssl._create_default_https_context = ssl._create_unverified_context
	url = f'https://finance.yahoo.com/quote/msft/financials?p={ticker}'
	headers = {'User-Agent': 'My User Agent 1.0',
		'From': f'https://finance.yahoo.com/quote/msft/financials?p={ticker}'
	}
	page = requests.get(url, headers=headers).text
	page_parsed = BeautifulSoup(page, 'html.parser')
	title = page_parsed.title.string
	if title == 'Symbol Lookup from Yahoo Finance':
		raise ValueError('ticker does not exist')
	tags = page_parsed.find_all(attrs={'data-test': 'fin-row'})
	rows = []
	for i in tags:
		rows.append(i.find(class_='Va(m)').get_text())
	if row not in rows:
		raise ValueError('row does not exist')
	elems = tags[rows.index(row)].find_all('span')
	return_tuple = []
	for i in elems:
		return_tuple.append(i.get_text())
	return return_tuple


if __name__ == '__main__':
	if len(sys.argv) == 3:
		print(get_row(sys.argv[1], sys.argv[2]))
	else:
		print('usage: python3 financial.py ticker field')