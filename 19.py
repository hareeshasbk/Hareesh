#functions to display hashtable
def display_hash(HashTable):
    for i in range(len(HashTable)):
        print(i,end="")

        for j in HashTable[i]:
            print("-->",end="")
            print(j,end="")

        print()

# creating hashtable as
# a nested list
HashTable=[[]for _ in range(10)]

# Hashing function to return
# key for every vlaue
def Hashing(keyvalue):
    return keyvalue % len(HashTable)


def insert(HashTable,keyvalue,value):
    hash_key=Hashing(keyvalue)
    HashTable[hash_key].append(value)

# driver code
insert(HashTable,10,'Allahabad')
insert(HashTable,25,'Mumbai')
insert(HashTable,20,'Mathura')
insert(HashTable,9,'Delhi')
insert(HashTable,21,'punjab')
insert(HashTable,21,'noida')

display_hash(HashTable)