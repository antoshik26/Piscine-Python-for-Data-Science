import sys
class Must_read(object):
	def __init__(self, file_name):
		self.file_name = file_name

	def file_reader(self):
		permission = self.file_name.split('.')
		if (permission[1] != 'csv'):
			raise ValueError('error')
		with open(self.file_name, 'r') as f:
			f_str = f.read()
		line = f_str.split('\n')
		if (len(line) < 2):
			raise ValueError('Too few lines')
		if (len(line[0].split(',')) != 2):
			raise ValueError('asdfg')
		for i in line[1:]:
			if (i != '1,0' and i != '0,1'):
				raise ValueError('asdf')
		return(f_str)

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		print("error")
		exit(1)
	e = Must_read(sys.argv[1])
	str_ret = e.file_reader()
	print(str_ret)