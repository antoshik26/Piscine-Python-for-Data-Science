import sys
from resource import *
import time


def loop(file_name):
	f_str = []
	with open(file_name, 'r') as f:
		f_str.append(f.read())
	return(f_str)

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		exit(1)
	new_list = loop(sys.argv[1])
	for i in new_list:
		pass
	# print(sys.getsizeof(new_list))
	# print(getrusage(RUSAGE_SELF))
	a = getrusage(RUSAGE_SELF)
	print(a.ru_maxrss / 1073741824)
	print(a.ru_utime + a.ru_stime)
	# print(getrusage(ru_utime) + getrusage(ru_stime))