import math
#1
"""
class UPPERCASEOKDA:
    getString = input()
    PrintString = print(getString.upper())
"""

#2

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, lenght):
        self.length = lenght
    def area(self):
        return self.length ** 2
class Cube(Square):
    def __init__(self, length):
        self.length = length
    def volume(self):
        self.volume = volume
        volume = self.length ** 3
        return self.length ** 3
        
length = float(input())
square = Square(length)
print(square.area())

"""
#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle(self):
        return self.length * self.width
length = float(input())
width = float(input())
superarea = Rectangle(length, width)
print(superarea.area())
"""
#4
# Point class is a collection of sets and points. BASICALLY AN XYZ COORDINATE WITH POINTS
"""
class PointClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(self.x, self.y)

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
"""    
"""
#5
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
            self.balance += amount
            print(self.balance)

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(self.balance)
            else:
                print("ERROR ERROR ERROR")

account = BankAccount(owner="Promotion Man", balance=float(input()))
account.deposit(float(input()))
account.withdraw(float(input()))
"""

"""
class BonkAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, plusmoney):
            self.balance += plusmoney
            return self.balance
    
    def withdraw(self, minusmoney):
        self.balance -= minusmoney
        if(self.balance < 0):
            print("ERROR ERROR ERROR")
        else:
            return self.balance
    

deposit = float(input())

withdraw = float(input())

ourmone = BonkAccount(owner = "Promotion Man", balance=float(input()))
ourmone.deposit(float(input()))
ourmone.withdraw(float(input()))
"""

#5
is_prime = lambda x: all(x%i != 0 for i in range(2, int(math.sqrt(x) + 1))) if x > 1 else False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

prime_numbers = list(filter(is_prime, numbers))

print(prime_numbers)
