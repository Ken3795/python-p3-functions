#!/usr/bin/env python3

def greet_programmer():
    '''prints "Hello, programmer!"'''
    print("Hello, programmer!")

def greet(name):
    '''prints "Hello, {name}!"'''
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    '''prints "Hello, {name}!" (with default to "programmer")'''
    print(f"Hello, {name}!")

def add(num1, num2):
    '''returns the sum of num1 and num2'''
    return num1 + num2

def halve(number):
    '''returns half of the given number (handles both int and float)'''
    return number / 2
