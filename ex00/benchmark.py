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

if __name__ == '__main__':
	setup = """from __main__ import loop, no_loop"""
	time_loop = timeit.timeit(setup=setup, stmt='loop()', number=9000)
	time_no_loop = timeit.timeit(setup=setup, stmt='no_loop()', number=9000)
	if (time_loop < time_no_loop):
		print('it is better to use a time_loop')
		print(str(time_loop) + 'vs' + str(time_no_loop))
	else:
		print('it is better to use a time_no_loop')
		print(str(time_no_loop) + ' vs ' + str(time_loop))