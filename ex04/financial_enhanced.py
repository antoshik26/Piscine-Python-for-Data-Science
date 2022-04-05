import sys
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import ssl


def get_row(ticker, row):
	ssl._create_default_https_context = ssl._create_unverified_context
	url = f'http://finance.yahoo.com/quote/{ticker}/financials'
	print(url)
	headers = {'User-Agent': 'My User Agent 1.0',
		'From': f'http://finance.yahoo.com/quote/{ticker}/financials'
	}
	page = urlopen(Request(url=url, headers=headers)).read()
	page_parsed = BeautifulSoup(page, 'html.parser')
	title = page_parsed.title.string
	if title == 'Symbol Lookup from Yahoo Finance':
		raise ValueError('ticker does not exist')
	tags = page_parsed.find_all(attrs={'data-test': 'fin-row'})
	rows = [tag.find(class_='Va(m)').get_text() for tag in tags]
	print(rows)
	if row not in rows:
		raise ValueError('row does not exist')
	elems = tags[rows.index(row)].find_all('span')
	return tuple(elem.get_text() for elem in elems)


if __name__ == '__main__':
	if len(sys.argv) == 3:
		print(get_row(sys.argv[1], sys.argv[2]))
	else:
		print('usage: python3 financial.py ticker field')