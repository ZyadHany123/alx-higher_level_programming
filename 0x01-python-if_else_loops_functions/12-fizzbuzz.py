#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 100):
        if n % 3 == 0:
            print("Fizz", end=" ")
        if n % 5 == 0:
            print("Buzz", end=" ")
        if n % 3 and n % 5:
            print("FizzBuzz", end=" ")
