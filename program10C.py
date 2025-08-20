numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even(num):
    return num % 2 == 0

x = list(filter(even, numbers))

print(x)
