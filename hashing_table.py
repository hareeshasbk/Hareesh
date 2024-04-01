def display_hash(HashTable):
    for i in range(len(HashTable)):
        print(i, end=" ")
        
        for j in HashTable[i]:
            print("---->", end=" ")
            print(j, end="")
    
        print()

HashTable=[[] for _ in range(10) ]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(HashTable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    HashTable[hash_key].append(value)

insert(HashTable, 10, 'allahabad')
insert(HashTable,  25, 'delhi')
insert(HashTable, 30, 'delhi')
insert(HashTable, 34, 'mathura')
insert(HashTable, 27, 'punjab')
insert(HashTable, 45, 'noida')
insert(HashTable, 24, 'lucknow')
insert(HashTable, 22, 'jaipur')
insert(HashTable, 23, 'agra')
insert(HashTable, 44, 'kanpur')

display_hash(HashTable)