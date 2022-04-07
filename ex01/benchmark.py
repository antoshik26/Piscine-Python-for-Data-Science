
import timeit
def loop():
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com',
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com',
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com',
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com',
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com']
	new_list = []
	for i in emails:
		if i.find('@gmail.com') != -1:
			new_list.append(i)
	return (new_list)

def no_loop():
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com',
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com',
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com',
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com',
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com']
	return [new_list for new_list in emails if(new_list.find('@gmail.com') != -1)]

def find(email):
	if(email.find('@gmail.com') != -1):
		return(email)
	pass
		
def map_loop():
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com',
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com',
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com',
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com',
			'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'panna@live.com', 'philipp@gmail.com']
	new_list = list(map(find, emails))
	return(new_list)

if __name__ == '__main__':
	setup = """from __main__ import loop, no_loop, map_loop"""
	time_loop = timeit.timeit(setup=setup, stmt='loop()', number=90000)
	time_no_loop = timeit.timeit(setup=setup, stmt='no_loop()', number=90000)
	time_map = timeit.timeit(setup=setup, stmt='map_loop()', number=90000)
	sort_time = []
	sort_time.append(time_loop)
	sort_time.append(time_no_loop)
	sort_time.append(time_map)
	sort_time.sort()
	print(sort_time)
	if (sort_time[0] == time_loop):
		print('it is better to use a loop')
		print(str(sort_time[0]) + ' vs ' + str(sort_time[1]) + ' vs ' + str(sort_time[2]))
	elif(sort_time[0] < time_no_loop):
		print('it is better to use a time_no_loop')
		print(str(sort_time[0]) + ' vs ' + str(sort_time[1]) + ' vs ' + str(sort_time[2]))
	else:
		print('it is better to use a time_map')
		print(str(sort_time[0]) + ' vs ' + str(sort_time[1]) + ' vs ' + str(sort_time[2]))
		