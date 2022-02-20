a=int(input("enter n:"))
list=[]
print("Enter number:")
for i in range(0,a):
    list.append(int(input()))
list.sort()
m=list[int(len(list))-1]
ans=0
for i in range(len(list)):
    if(list[i]<m):
        if(ans<list[i]):
            ans=list[i]

print(ans)











