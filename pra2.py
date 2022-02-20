# Name : Shail shah
# ID : 20CE134
# Aim :  You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa. Sample Input: HackerRank.com presents "Pythonist 2".
# Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".
string=input("enter string:")
def str(stri):
    num=""
    for i in string:
      if(i.isupper()):
          num+=(i.lower())
      else:
          num+=i.upper()
    return  num
print(str(string))
