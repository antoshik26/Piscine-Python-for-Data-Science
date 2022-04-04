class Must_read:
	with open('data.csv', 'r') as f:
		f_str = f.read()
	print(f_str)

if __name__ == '__main__':
	Must_read