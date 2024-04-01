#Python program to implement non primitive data type

import array as arr 

a=arr.array('i',[])

#take input list size
n=int(input("Enter value for array size:"))

for i in range(n):
    #append element in  array/list
    x=int(input("Enter the array of elements:"))
    a.append(x)

print(a)

for i in range (n):
    print(a[i])


print("reverse of element")
for i in range (len(a)-1,-1,-1):
    print(a[i])


