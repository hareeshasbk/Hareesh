#Program Python program to implement stack.

def create_stack():
    STACK=[]
    return STACK

def push(STACK,item):
   STACK.append(item) 
   print("Pushed item = ", item)
   
def pop(STACK):
    if(len(STACK)==0):
        print("Stack is empty")
    else: 
        return (STACK.pop())
    
def selectOption(ch):
    if ch==1:
        x = int(input("Enter value for push = "))
        push(STACK, x)
    else:
        x=pop(STACK) 
        print("Popped element from Stack =", x)
        
        
STACK=create_stack()
ch=0

while(ch<3):
    print("------Stack-------")
    print("1 Push" )
    print("2 Pop")
    print("3 Exit ")
    print("----------------------------")
    
    ch=int(input("Enter your choice ="))
    selectOption(ch)
    print(STACK)

