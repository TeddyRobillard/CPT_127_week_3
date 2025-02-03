
# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.



# Problem 1: Write a program that takes a list of numbers and prints out the sum of all the numbers in the list.

Sumlist = input("Type in a list for a sum: ")
Sumlist = [float(x) for x in Sumlist.split(', ')]
TheNumber = sum(Sumlist)
BetterNumber = '%g'%(TheNumber)
print(BetterNumber)
# Problem 2: Write a program that takes a list of numbers and prints out the average of all the numbers in the list.

Averagelist = input("Type in a list for a average: ")
Averagelist = [float(x) for x in Averagelist.split(', ')]
AverageNumber = sum(Averagelist) / len(Averagelist)
BetterAverageNumber = '%g'%(AverageNumber)
print(BetterAverageNumber)

# Problem 3: Write a program that takes a list of numbers and prints out the largest number in the list.

BiggestNumberlist = input("Type a list for the biggest number: ")
BiggestNumberlist = [float(x) for x in BiggestNumberlist.split(', ')]
BiggestNumber = max(BiggestNumberlist)
BigBoi = '%g'%(BiggestNumber)
print(BigBoi)