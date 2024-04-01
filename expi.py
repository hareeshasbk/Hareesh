def binary_search (list,low,high,s):
    if high>=low:
        mid=(high+low)//2
        if list [mid]==s:
            return mid
        elif list[mid]>s:
            return binary_search(list,low,mid-1,s)
        else:
            return binary_search(list,mid+1,high,s)
    else:
        return -1
# define list
list=[]
size=int(input("Enter the list size:"))

for i in range(size):
    #append element in list
    n=int(input(f"Enter list of {i} element:"))
    list.append(n)
s=int(input("Enter element to search:"))
#function call 
result =binary_search(list,0,len(list)-1,s)
if result!=-1:
    print("Element is found at index",str(result))
else:
    print("Element not found in list")