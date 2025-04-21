import psycopg2

"""
lst = list(map(int, input().split(' ')))
print(lst)
"""

lst = []
filename = 'lst.txt'
with open(filename, 'r') as file:
    contents = file.read()[1:-1]
    lst = 
