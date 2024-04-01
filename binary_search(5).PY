#Python program to implement binary search

def binary_search (A,low,high,s):
    if high>=low:
        mid=(high+low)//2
        if A [mid]==s:
            return mid
        elif A[mid]>s:
            return binary_search(A,low,mid-1,s)
        else:
            return binary_search(A,mid+1,high,s)
    else:
        return -1
# define A
A=[]
size=int(input("Enter the A size:"))

for i in range(size):
    #append element in A
    n=int(input(f"Enter A of {i} element:"))
    A.append(n)
s=int(input("Enter element to search:"))
#function call 
result =binary_search(A,0,len(A)-1,s)
if result!=-1:
    print("Element is found at index",str(result))
else:
    print("Element not found in A")



