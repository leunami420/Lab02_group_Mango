list1 = []

for i in range(1,21):
    list1.append(i)
print(list1)

#part2.1
squaresOfList1 = []

for x in range(0,20):
    squaresOfList1.append(list1[x]**2)
print(squaresOfList1)

#part2.2
evenList = []

for numbers in range(1,21):
    if numbers % 2 == 0:
        evenList.append(numbers)
print(evenList)




