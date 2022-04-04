import sys
import os
class Must_read():
	def __init__(self, file_name):
		self.file_name = file_name
		line = self.file_reader()
		self.count = self.Calculations.counts(line)
		self.fraction = self.Calculations.fractions(line)

	def file_reader(self, has_header = True):
		permission = self.file_name.split('.')
		if (has_header == True):
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
		print(line[1:])
		return(line[1:])

	class Calculations:
		def counts(line):
			count_0 = 0
			count_1 = 0
			for i in line:
				if (i == '0,1'):
					count_1 += 1
				else:
					count_0 += 1
			return (count_0, count_1)

		def fractions(line):
			count_0 = 0
			count_1 = 0
			for i in line:
				if (i == '0,1'):
					count_1 += 1
				else:
					count_0 += 1
			new_count_0 = count_0 / len(line)
			new_count_1 = count_1 / len(line)
			return (new_count_0, new_count_1)

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		print("error")
		exit(1)
	e = Must_read(sys.argv[1])
	print(e.count)
	print(e.fraction)