"""
def squares(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input())
for square in squares(n):
    print(square, end=" ")
"""

"""
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
even_numbers = even_numbers(n)
print(", ".join(str(num) for num in even_numbers))
"""

"""
def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in divisible(n):
    print(num, end=" ")
"""

"""
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input())
b = int(input())

for square in squares(a, b):
    print(square, end=" ")
"""

"""
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for num in countdown(n):
    print(num, end=" ")
"""


