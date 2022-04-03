import sys
if __name__ == "__main__":
	if (len(sys.argv) != 2):
		exit(1)
	COMPANIES = {'Apple': 'AAPL','Microsoft': 'MSFT','Netflix': 'NFLX','Tesla': 'TESLA','Nokia': 'NOKIA'}
	STOCKS = {'AAPL': 287.73, 'MSFT': 173.79, 'NFLX': 416.90,'TSLA': 724.88,'NOK': 3.37}
	if sys.argv[1] not in COMPANIES:
		print('Unknown company')
	else:
		print(STOCKS[COMPANIES[sys.argv[1]]])