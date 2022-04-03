import sys
if __name__ == "__main__":
	if (len(sys.argv) != 2):
		exit(1)
	with open(sys.argv[1], 'r') as file:
		array = [row.strip() for row in file]
	my_file = open("employees.tsv", "w")
	my_file.write('Name\t Surname\t E-mail\n')
	for i in array:
		a = i.split("@")
		name, sername = a[0].split('.')
		my_file.write(name + '\t ' + sername + '\t ' + i + '\n')
	my_file.close()