lst = list(map(int, input().split(' ')))

filename = 'lst.txt'

with open (filename, 'w') as file:
    file.write(str(lst))

with open (filename, 'r') as file:
    contents = file.read()[1:-1]
    lst = list(map(int, contents.split(', ')))

print(lst)