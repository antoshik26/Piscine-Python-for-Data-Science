import sys
if __name__ == "__main__":
	if (len(sys.argv) != 2):
		exit(1)
	COMPANIES = {'Apple': 'AAPL','Microsoft': 'MSFT','Netflix': 'NFLX','Tesla': 'TSLA', 'Nokia': 'NOK'}
	STOCKS = {'AAPL': 287.73, 'MSFT': 173.79, 'NFLX': 416.90,'TSLA': 724.88,'NOK': 3.37}
	flag = False
	new_str_company = []
	str_company = sys.argv[1].split(',')
	for i in str_company:
		new_str_company.append(i.replace(' ', ''))
	for i in new_str_company:
		if (i.upper() in STOCKS):
			for j in COMPANIES.items():
				if (i.upper() == j[1]):
					print(i.upper() + ' is a ticker symbol for ' + j[0])
					flag = True
		else:
			for k in COMPANIES:
				if (k.lower() == i.lower()):
					print(k + ' stock price is ' + str(STOCKS[COMPANIES[k]]))
					flag = True
		if (flag == False):
			print(i + ' is an unknown company or an unknown ticker symbol')
		else:
			flag = False