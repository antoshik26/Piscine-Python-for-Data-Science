class Must_read:

	def file_reader():
		with open('data.csv', 'r') as f:
			f_str = f.read()
		return(f_str)

if __name__ == '__main__':
	str_ret = Must_read.file_reader()
	print(str_ret)