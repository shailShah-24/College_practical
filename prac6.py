 #Name :Shail Shah
# ID : 20CE134
# Aim :  You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

words = []
repeated = []
occurrence = []
dict = {}
n = int(input())

for i in range(n):
    stru = input()
    words.append(stru)

def countX(words, x):
    count = 0
    for ele in words:
        if (ele == x):
            count = count + 1
    return count

for i in words:
    dict[i] = countX(words,i)

l = dict.values()

a = len(l)
print(a)

print(' '.join(map(str,l)))