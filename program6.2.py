#program6:-python program to implement bubble sort
a=[]
n=0
def display():
    print ("sorted list=",a)

def read():
    for i in range(n):
        a.append (int(input(f"enter {i} element:")))

def bubbleSort():
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
            display()
        print("....................i=",i)

n=int(input("enter size of list:"))
read()
bubbleSort()
display()
