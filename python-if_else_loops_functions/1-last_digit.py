#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_d = ((number * -1) % 10) * -1
else:
    last_d = number % 10
if number > 5:
    print(f"Last digit of {number} is {last_d} and is grater than 5")
elif number == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
else:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
