#program6:-python program to implement bubble sort
a=[]
n=int(input("enter the total number of elements:"))
for i in range(n):
    value=int(input(f"enter {i} element:"))
    a.append(value)

for i in range (n-1):
    for j in range (n-i-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print("this result in ascending order:",a)
