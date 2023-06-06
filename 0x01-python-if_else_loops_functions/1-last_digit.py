#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
expression = "Last digit of {} is {}".format(number, last_digit)
if number < 0 and last_digit != 0 :
    last_digit = -last_digit
if last_digit > 5:
    print("{} and is greater than 5".format(expression))
elif last_digit == 0:
    print("{} and is 0".format(expression))
elif last_digit < 6 and last_digit != 0:
    print("{} and is less than 6 and not 0".format(expression))
