import timeit
import sys
from collections import Counter
from random import randint

def loop(list_rand):
	d = dict()
	for i in list_rand:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
	return (d)

def top_loop(list_rand):
	d = dict()
	for i in list_rand:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
	sort_d = []
	for i in range(10):
		a = sorted(d.items(), key =lambda x: -x[1])
		sort_d.append(a)
	return (sort_d)

def Counter_counter(list_rand):
	return (Counter(list_rand))

def top_Counter(list_rand):
	ls = Counter(list_rand).most_common(10)
	return(ls)


if __name__ == '__main__':
	new_list = [randint(0, 100) for i in range(1000000)]
	setup = """from __main__ import loop, top_loop, Counter_counter, top_Counter"""
	time_loop = timeit.timeit(setup=setup, stmt=f'loop({new_list})', number=1)
	print('my function: ' + str(time_loop))
	time_count = timeit.timeit(setup=setup, stmt=f'Counter_counter({new_list})', number=1)
	print('Counter: ' + str(time_count))
	time_filter = timeit.timeit(setup=setup, stmt=f'top_loop({new_list})', number=1)
	print('my top: ' + str(time_filter))
	time_count_top = timeit.timeit(setup=setup, stmt=f'top_Counter({new_list})', number=1)
	print('Counter\'s top: ' + str(time_count_top))