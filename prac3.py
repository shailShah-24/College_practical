k=int(input())
list=[]
input_string = input()
print("\n")
user_list = input_string.split()

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])
b=int(len(user_list))
ar= b/k;
for i in range(0,len(user_list)):
    if(user_list[i]>ar):
        print(user_list[i])
        break




