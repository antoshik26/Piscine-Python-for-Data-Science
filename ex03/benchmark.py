import timeit
import sys
from functools import reduce
def loop(count):
	a = 0
	for i in range(0, count):
		a = a + i * i
	return (a)

def reduse_loop(count):
	sum_all = reduce(lambda x,y: x + y*y, range(0, count))
	return (sum_all)

if __name__ == '__main__':
	if len(sys.argv) != 4:
		exit(1)
	if (str.isdigit(sys.argv[2]) == -1):
		exit(1)
	if (str.isdigit(sys.argv[3]) == -1):
		exit(1)
	count = 5
	# count = sys.argv[3]
	setup = """from __main__ import loop, reduse_loop"""
	if (sys.argv[1] == 'loop'):
		time_loop = timeit.timeit(setup=setup, stmt=f'loop({count})', number=int(sys.argv[2]))
		print(time_loop)
	if (sys.argv[1] == 'reduse'):
		time_filter = timeit.timeit(setup=setup, stmt=f'reduse_loop({count})', number=int(sys.argv[2]))
		print(time_filter)