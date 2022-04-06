import financial
import cProfile

if __name__ == '__main__':
	str_test = cProfile.run('financial.get_row("MSFT", "Total Revenue")')
	print(type(str_test))
	'python3 -m cProfile -s cumtime financial.py 'MSFT' 'Total Revenue' > profiling-sleep.txt'