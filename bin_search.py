# Python program to implement binary search

a=[]
n=int(input("Enter the size of list: "))

for i in range(n):
    a.append(int(input(f"Enter the element to {i}: ")))

print(a)


s=int(input("Enter the element to search: "))

def Binary_Search(a,low,high,s):
    if a[high]>=a[low]:
        mid=(low+high)//2
        if a[mid]==s:
            return mid
        elif a[mid]>s:
            return Binary_Search(a,low,mid-1,s)
        else:
            return Binary_Search(a,mid+1,high,s)
    else:
        return -1
    
result=Binary_Search(a,0,len(a)-1,s)

if result!=-1:
    print("The element is found at index",str(result))
else:
    print("The element is not found")
