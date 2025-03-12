def generator(n):
    for i in range (1, 6):
        yield i

n = int(input())
for square in generator(n):
    print(square, end=" ")