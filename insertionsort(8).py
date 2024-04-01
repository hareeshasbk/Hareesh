# python program to implement insertion sort

def Read():
    for i in range(size):
        x=int(input(f"Enter the element {i}:"))
        A.append(x)


def Display():
    print("List=",A)


def InsertionSort(A):
    for i in range(1,len(A)):
        key=A[i]
        j=i-1
        while j>=0 and key<A[j]:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key


A=[]
size=int(input("Enter the size of list="))


Read()
Display()
InsertionSort(A)
Display()
