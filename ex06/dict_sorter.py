if __name__ == "__main__":
	list_of_tuples = [
	('Russia', '25'),
	('France', '132'),
	('Germany', '132'),
	('Spain', '178'),
	('Italy', '162'),
	('Portugal', '17'),
	('Finland', '3'),
	('Hungary', '2'),
	('The Netherlands', '28'),
	('The USA', '610'),
	('The United Kingdom', '95'),
	('China', '83'),
	('Iran', '76'),
	('Turkey', '65'),
	('Belgium', '34'),
	('Canada', '28'),
	('Switzerland', '26'),
	('Brazil', '25'),
	('Austria', '14'),
	('Israel', '12')]
	new_list = dict()
	new_list = {key: int(value) for key, value in list_of_tuples}
	for elem in sorted(new_list.items(), key=lambda x: (x[1], x[0]), reverse = True):
		print(elem[0])