# functions.py
import math
import random
import itertools

"""
def grams_to_ounces(grams):
    grams=float(input())
    return 28.345 * grams
"""

"""
def celsius(fahrenheit):
    fahrenheit=float(input())
    return (5 / 9) * (fahrenheit - 32)
"""

"""
def solve(heads, legs):
    for chickens in range(numheads + 1):
        rabbits = heads - chickens
        if (2 * chickens + 4 * rabbits) == legs:
            return chickens, rabbits
    return None
"""

"""
def prime(n):
    if n <= 1:
        return False
    for i in range(2, math.sqrt(int(n)) + 1):
        if n % i == 0:
            return False
    return True
"""

"""
def filter(num):
    num = list(map(int, input().split()))
    return [num for num in num if prime(num)]
"""

"""
def string_permutations(s):
    s=input()
    return [''.join(p) for p in permutations(s)]
"""

"""
def reverse_words(sentence):
    sentence = input()
    sentence.split()
    sentence.reverse()
    return ' '.join(words)
"""

"""
def has_33(num):
    for i in range(len(num) - 1):
        if num[i] == 3 and num[i + 1] == 3:
            return True
    return False
"""
    
"""
def spy_game(num):
    num = list(map(int, input().split()))
    sequence = [0, 0, 7]
    for i in range(len(num) - 2):
        if num[i:i+3] == sequence:
            return True
    return False
"""

"""
def sphere(radius):
    radius=float(input())
    return (4 / 3) * pi * radius**3
"""

"""
def unique(lst):
    lst = list(map(int, input().split()))
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
"""

"""
def pal(s):
    s = input()
    s = s.replace(" ", "").lower()
    return s == s[::-1]
"""

"""
def histogram(lst):
    lst = list(map(int, input().split()))
    for num in lst:
        print('*' * num)
"""

"""
def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
"""