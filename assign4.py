
# Given a list of integers, write a program to print the count of all possible unique combinations of numbers whose sum is equal to K. Input The first line of input will contain space-separated integers. The second line of input will contain an integer, denoting K. Output The output should be containing the count of all unique combinations of numbers whose sum is equal to K.
from itertools import combinations

values =[int(i) for i in input('Enter space-separated integers: ').split()]
values.sort()

K = int(input('Enter K: '))
counterUniqueCombinations=0
print("The unique combinations with the sum equal to "+str(K)+" are:")
for i in range(1, len(values)+1):
    com =list(set(combinations(values, i)))
    for combination in com:
        if sum(combination) == K:
            print(combination)
            counterUniqueCombinations += 1
print("The count of all unique combinations is: "+str(counterUniqueCombinations))