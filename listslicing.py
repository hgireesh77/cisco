list1=["Grapes", "1",2,3,"Oranges"]
#--------------------------------Indexing and printing---------------------------
print(list1) #prints the whole list
print(list1[0]) #prints the first value which is index 0 that is Grapes
print(list1[0:1]) #prints the values until index 1 but not the value in index 1
print(list1[1:2]) #same as above but the second value
print(list1[1:]) #prints all the values from index 1 omitting Grapes
print(list1[:4]) #prints all the values from index 0 ommiting Oranges
print(list1[0:5]) #since the index value given is 5 which is greater than the original index value it prints all the values in the list
print(list1[-1]) #prints the last item in the list which is at the right most end
print(list1[0:-2]) #prints the items from left until 3rd last item which will be "'Grapes', 1, 2"
print(list1[-2:]) #prints the items from right until 2nd last item which will be "3,'Oranges'"
print(list1[-4:-2]) #prints the items from left until 2nd last item but not the 2nd last item which will be "1, 2"
print(list1[-2:-4]) #this will not print anything
print(list1[::1], list1[::-1], sep="/") # this will print forward and reverse the list items
#--------------------------------Different functions of list---------------------
print(len(list1))
a=2
b=3
c=(a**2) + (b**2)
print(a,b,(a**2),(b**2),c)
f_name="Gireesh"
l_name="Hariharasubramony"
print(f_name, l_name, sep='.')
print(type(10/10),type(10*10))
number_of_moons = 79
sentence = "The total number of (known) moons for the planet Jupiter is " + str(number_of_moons)
print(sentence)

age_in_years = int(input("What is your age? "))
age_in_months = age_in_years * 12
print("Your age in months is: ", age_in_months)