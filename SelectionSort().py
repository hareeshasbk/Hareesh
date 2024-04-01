n=int(input("Enter the size of list:"))
A=[]

def read():
    for i in range(n):
        A.append(int(input("Enter the elements:")))

def display():
    print("List:",A)

def SelectionSort():
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if A[j]<A[min]:
                min=j
        A[i],A[min]=A[min],A[i]

read()
SelectionSort()
display()









