def read_and_write():
	with open('hh.csv', 'r') as f:
		f_str = f.read()
	f_str = f_str.replace(',', '\t')
	print(f_str)
	with open('hh.tsl', 'w') as f:
		f.write(f_str)
if __name__ == '__main__':
	read_and_write()