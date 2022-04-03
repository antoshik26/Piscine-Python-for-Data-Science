import sys
if __name__ == "__main__":
	if (len(sys.argv) != 2):
		exit(1)
	with open('employees.tsv', 'r') as file:
		array = [row.strip() for row in file]
	for i in array:
		if (i.find(sys.argv[1]) != -1):
			name, sername, emale = i.split('\t')
			break
	if name:
		name = name.capitalize()
		print(f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.')