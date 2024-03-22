#program4:-python program to implement linear search
#define list
A=[]

#take input list size
size=int(input("enter size of list :"))

for i in range(size):
    n=int(input(f"enter {i} element:"))
    A.append(n)

s=int(input("enter number to search in list:"))

flag=0

for i in range(size):
    if s==A[i]:
        flag=1
        break

if flag==1:
    print(f"{s} was found in the index {i}")
else:
    print(f"{s} was not found")
