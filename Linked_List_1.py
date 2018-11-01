

class Node:
    def __init__(self,data=None):
        self.data= data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node()
    
    def append(self,data):
        new_node=Node(data)
        current_node1=self.head
        while not current_node1.next is None:
            current_node1=current_node1.next
        current_node1.next=new_node

    def length(self):
        count=1
        current_node1=self.head
        while not current_node1.next is None:
            count+=1
        return count
    
    def delete(self,index):
        if self.length()<index:
            return ("Value does not exist at this index")   
        else:
            current_node1=self.head
            count=0
            while not current_node1.next is None:
                lastnode=current_node1
                current_node1=current_node1.next
                if count==index:
                    lastnode.next=current_node1.next
                    return 
                count+=1


    
    def get(self,index):
        if index >= self.length():
            return "Index is greater than the linked list value"
        count=0
        current_node1=self.head
        while not current_node1.next is None:
            current_node1=current_node1.next
            print("Hi")
            if index==count:
                return current_node1.data
                
            count+=1
            
    
    def swapnode(self,key1,key2):
        if key1==key2:
            return
        current_node1= self.head
        current_node2=self.head
        previous_node1=None
        previous_node2=None
        # Finding key 1
        while current_node1 and current_node1.data!=key1:
            previous_node1=current_node1
            current_node1=current_node1.next
        #Finding key 2 
        while current_node2 and current_node2.data!=key2:
            
            previous_node2=current_node2
            current_node2=current_node2.next

        if not current_node1 or not current_node2:
            return

        if previous_node1:
            previous_node1.next=current_node2
           
        else:
            self.head=current_node2
        if previous_node2:                
            previous_node2.next=current_node1    
            print(previous_node2.data)
        else:
            self.head=current_node1
            


    def displaylist(self):
        current_node=self.head
        elements=[]
        while not current_node.next is None:
            current_node=current_node.next
            elements.append(current_node.data)
            
        return elements

    # def reverselist(self):
    #     # a->b->c->d
    #     previous_node=None
    #     current_node=self.head
    #     while current_node:
    #         current_node.next=previous_node
    #         previous_node=current_node
    #         current_node=current_node.next
    #         self.head=current_node 

llist=LinkedList()   
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.swapnode("C","D")
print(llist.displaylist())
            


