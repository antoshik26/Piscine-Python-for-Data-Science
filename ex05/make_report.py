from analytics import *
from config import *

if __name__ == '__main__':
	e = Must_read(file_name)
	count = e.count[0] + e.count[1]
	count_0 = e.count[0]
	count_1 = e.count[1]
	fraction = e.fraction
	a = Analytics(e.line)
	list_predict = a.predict_random(3)
	tail = 0
	heads = 0
	for i in list_predict:
		if (i[1] == 0):
			tail += 1
		else:
			heads += 1
	text = (f"""Report
We have made {count} observations from tossing a coin: {count_0} of them were tails and {count_1} of
them were heads. The probabilities are {fraction[0]}\% and {fraction[1]}\%, respectively. Our
orecast is that in the next {num_steps} observations we will have: {tail} tail and {heads} heads.""")
	a.file_print(output_file, text)