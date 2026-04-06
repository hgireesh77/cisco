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

#function to find a word is Palindrome

#list1 is "Malayalam"
#list1 is "Hello"

def palindrome(list1):
  Palin = False
  mid = len(list1)//2

  for i in range(0,mid):
    if list1[i] == list1[(len(list1)-1)-i]:
      Palin = True
      continue

  return Palin

print(f"Palindrome: {palindrome('Malayalam')}")

#function so reverse the string
#The string is "Hello"

def reverse(string1):
  rev = []

  for i in range(0, len(string1)):
    rev.insert(-i,string1[i])

  print("".join(rev))

reverse("Hello")
string1 = "Hello"
print(string1[::-1])

#function to provide a distinct list from the given list which have repeated elements
# list1 = [1,2,3,1,4,2,5,6,7,4,6,8,9,7]

def dist(list1):
  dist_list = []
  for i in list1:
    if i not in dist_list:
      dist_list.append(i)

  print(f"The unique list is: {dist_list}")

dist([1,2,3,1,4,2,5,6,7,4,6,8,9,7])

#Function to find a number is Prime or not

def prime(num1):
  if num1 < 1:
    print(f"{num1} is not Prime and it is less than 1")
  else:
    if num1 == 1 or num1 == 2 or num1 == 3 or num1 == 5:
      print(f"{num1} is Prime")
    else:
      p = str(num1)
      l = len(p)

      if p[l-1] == '1' or p[l-1] == '3' or p[l-1] == '7' or p[l-1] == '9' and l>1:
        print(f"{num1} is Prime")
      else:
        print(f"{num1} is not Prime")

prime(10)
prime(9)
prime(5)
prime(20)
prime(1)
prime(0)
prime(-1)