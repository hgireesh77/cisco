list1 = [1,2,3,4,5,6,6,6,6,6,7]
dict = {"k1":"v1", "k2":"v2"}
set1 = set(list1)
tuple1 = tuple(list1)


for i in tuple1:
    print(f"{i}")

for i in set1:
    print(i)

print(len(tuple1))

for i in range(len(tuple1)):
    print(f"{tuple1[i]}")

for x,y in dict:
    print(x, y)

prices = {"apple": 1.0, "banana": 0.5}
# Double all prices
discounted_prices = {k: v * 2 for k, v in prices.items()}
print(discounted_prices)