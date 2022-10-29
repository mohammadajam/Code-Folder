from random import randint

unique_number_list = []

for i in range(100000):
	n_1 = randint(1,1e5)
	n_2 = randint(1,1e5)

	num = n_1*n_2
	num_digits = [*str(num)]
	if '0' in num_digits and '1' in num_digits and '2' in num_digits and '3' in num_digits and '4' in num_digits and '5' in num_digits and '6' in num_digits and '7' in num_digits and  '8' in num_digits and '9' in num_digits:
		unique_number_list.append([n_1,n_2,num])

for number in unique_number_list:
	print(number)