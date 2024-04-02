
def towerofhanoi(n, rodA, rodB, rodC):
    if n == 0:
        return
    towerofhanoi(n - 1, rodA, rodB, rodC)
    print(f"Move disk {n} from {rodA} to {rodC}")
    towerofhanoi(n - 1, rodB, rodC, rodA)

n = int(input("Enter the number of disks: "))
towerofhanoi(n, 'P', 'Q', 'R')


