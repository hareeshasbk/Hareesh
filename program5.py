#program5:-python program to implement binary search
def binary_search(A,low,high,s):
    if high>=low:
        mid=(high+low)//2
        if A[mid]==s:
            return mid
        elif A[mid]>s:
            return binary_search(A,low,mid-1,s)
        else:
            return binary_search(A, mid+1,high, s)
    else:
        return -1


#define list
A=[]
size=int(input("enter the size of the list:"))

for i in range (size):
    A.append(int(input("enter element:")))

s=int(input("enter which element you want to search:"))

result=binary_search(A,0,size-1,s)

if result==-1:
    print("element is not found")
else:
    print("element is found")






