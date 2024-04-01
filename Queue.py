def create_Queue():
    Queue=[]
    return Queue

def Insert(Queue,item):
    Queue.append(item)
    
def Delete(Queue):
    if(len(Queue)==0):
        return "Queue is empty"
    else:
        return (Queue.pop(0))
def selectOption(ch):
    if ch==1:
        x=int(input("Enter the item to insert:"))
        Insert(Queue,str(x))
    elif ch==2:
        print("Delete item:",Delete(Queue))    

Queue=create_Queue()
ch=0
while ch<3:
    print(" 1 Insert")
    print(" 2 Delete ")
    print(" 3 Exit")
    ch=int(input("Enter your choice:"))
    selectOption(ch)
    print (Queue)
    