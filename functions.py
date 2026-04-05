def multiply(lst):
    pdt = 1
    for i in lst:
        pdt = pdt * int(i)

    print(pdt)


lst = [10,20,30,40]
multiply(lst)


def rev(x):
    str = x[::-1]
    print(str)

rev("Hello")

def numRange(start, stop, num):
    if num>=start and num<=stop:
        print(f"{num} is between {start} and {stop}")

print(numRange(5,10,6))

def uniquelist(lst):
    ulst = set(lst)
    print(ulst)

uniquelist([1,1,2,2,3,3])

