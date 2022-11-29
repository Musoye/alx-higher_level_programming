#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
if last_digit > 5:
	if str(number)[0] == '-':
		print(f'Last digit of {number:d} is -{last_digit:d} and is
greater than 5')
	else:
		print(f'Last digit of {number:d} is {last_digit:d} and is
greater than 5')
else:
	if str(number[0]) == '-':
		print(f'Last digit of {number:d} is -{last_digit:d} and is less than 6 and not 0')
	else:
		print(f'Last digit of {number:d} is {last_digit:d} and is less than 6 and not 0')
