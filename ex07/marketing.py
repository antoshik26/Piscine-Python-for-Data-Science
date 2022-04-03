import sys
def call_center(clients, participants, recipients):
	call = []
	for i in participants:
		if (i not in clients and i not in call):
			call.append(i)
	for i in recipients:
		if (i not in clients and i not in call):
			call.append(i)
	return (call)

def potential_clients(clients, participants, recipients):
	potential = []
	for i in clients:
		if (i not in participants and i not in potential):
			call.append(i)
	for i in recipients:
		if (i not in participants and i not in potential):
			call.append(i)
	return potential

def loyalty_program(clients, participants, recipients):
	loyalty = []
	for i in clients:
		if (i not in recipients and i not in loyalty):
			loyalty.append(i)
	for i in participants:
		if (i not in recipients and i not in loyalty):
			loyalty.append(i)
	return loyalty


if __name__ == "__main__":
	clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
	participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
	recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
	new_list = []
	if (len(sys.argv) != 2):
		exit(1)
	if (sys.argv[1] == 'call_center'):
		new_list = call_center(clients, participants, recipients)
	elif (sys.argv[1] == 'potential_clients'):
		new_list = potential_clients(clients, participants, recipients)
	elif (sys.argv[1] == 'loyalty_program'):
		new_list = loyalty_program(clients, participants, recipients)
	else:
		raise ValueError('Unknown command')
	for i in new_list:
		print(i)
