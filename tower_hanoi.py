def towerofhanoi(n,rodA,rodB,rodC):
    if n==0:
        return
    towerofhanoi(n-1, rodA, rodB,rodC)
    print("move disk", n,"rodA", rodA,"rodB", rodB)
    towerofhanoi(n-1,rodC,rodB,rodB)
n=int(input("enter number of disks:"))
towerofhanoi(n,'P','Q','R')


