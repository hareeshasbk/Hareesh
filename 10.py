class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def Insert(self,x):
        newnode=Node(x)
        newnode.next=self.head
        self.head=newnode

    def Delete(self):
        temp=self.head
        if temp:
            self.head=temp.next
            temp.next=None
            print("Deleted Node ="+str(temp.data))
        else:
            print("list is empty,")

    def Display(self):
        temp=self.head
        if(temp):
            print("Linkedlist---> ", end="")
            while(temp):
                print(str(temp.data)+"  ",end="")
                temp=temp.next
        else:
            print("list is empty")

    def searchNode(self):
        flag=0
        x=int(input("Enter which node you wnt to search="))
        temp=self.head

        if(temp):

            while(temp):
                if x==temp.data:
                    flag=1
                    break
                temp=temp.next

            if (flag==1):
                print("element is found in list")
            else:
                print("element not found in list")
        else:
            print("list is empty")



if __name__=='__main__':
    LL=Linkedlist()
    ch=1
    while ch<=4:
        print("----------Menu--------")
        print("1. Insert node at begining")
        print("2. delete  ")
        print("3. Display  ")
        print("4. search")

        ch=int(input("enter your choice="))
        if ch==1:
            x=int(input("Enter value for node="))
            LL.Insert(x)
        elif ch==2:
            LL.Delete()
        elif ch==3:
            LL.Display()
        elif ch==4:
            LL.searchNode()
            print()
            print()
