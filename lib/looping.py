#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")
    return 
happy_new_year()

def square_integers(int_list):
    squared_list = [(int) ** 2 for int in int_list]
    print(squared_list)
    return squared_list
    

def fizzbuzz():
    num = 0
    while num < 100:
        num += 1 
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else: 
            print(num)
    

