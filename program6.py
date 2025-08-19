def number():
    num=2
    count=0

    while count < 5:
        yield num
        num +=2
        count +=1

for even in number():
        print(even)
