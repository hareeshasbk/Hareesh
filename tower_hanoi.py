def towerofhanoi(n, rodA, rodB, rodC):
    if n == 0:
        return
    towerofhanoi(n - 1, rodA, rodC, rodB)
    print(f"Move disk {n} from {rodA} to {rodB}")
    towerofhanoi(n - 1,  rodC,rodB, rodA)

n = int(input("Enter the number of disks: "))
towerofhanoi(n, 'P', 'Q', 'R')
