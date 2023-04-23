#a list between 1 and 20
list1 = []

for i in range(1,21):
    list1.append(i)
print(list1)

#aufgabe1.1
squaresOfList1 = []

for x in range(0,20):
    squaresOfList1.append(list1[x]**2)
print(squaresOfList1)

#aufgabe1.2
evenList = []

for numbers in list1:
    if numbers % 2 == 0:
        evenList.append(numbers)
print(evenList)

#aufgabe2.1



