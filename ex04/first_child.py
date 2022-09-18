import sys
import os
import random

class Must_read():
	def __init__(self, file_name):
		self.file_name = file_name
		self.line = self.file_reader()
		self.c = self.Calculations(self.line)
		self.count = self.c.counts()
		self.fraction = self.c.fractions()

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
		#print(line[1:])
		return(line[1:])

	class Calculations:
		def __init__(self, line):
			self.new_line = line
			count = self.counts()
		
		def counts(self):
			count_0 = 0
			count_1 = 0
			for i in self.new_line:
				if (i == '0,1'):
					count_1 += 1
				else:
					count_0 += 1
			return (count_0, count_1)

		def fractions(self):
			count_0 = 0
			count_1 = 0
			for i in self.new_line:
				if (i == '0,1'):
					count_1 += 1
				else:
					count_0 += 1
			new_count_0 = count_0 / len(self.new_line)
			new_count_1 = count_1 / len(self.new_line)
			return (new_count_0, new_count_1)

class Analytics(Must_read.Calculations):
	def predict_random(self, count):
		dictionary = {0: [0, 1], 1: [1, 0]}
		return [dictionary[random.randint(0, 1)] for i in range(count)]

	def predict_last(self):
		return (self.new_line[len(self.new_line) - 1])
	
	def file_print(self, file_name, text):
		with open(file_name, 'w') as f:
			f.write(text)

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		print("error")
		exit(1)
	e = Must_read(sys.argv[1])
	print(e.file_reader())
	print(e.count)
	print(e.fraction)
	a = Analytics(e.line)
	list_predict = a.predict_random(3)
	print(list_predict)
	print(a.predict_last())