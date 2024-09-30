class ListNode():

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
    
class LinkedList():

    head = None
    tail = None
    length = 0
    
    def append(self, data):

        newNode = ListNode()
        newNode.val = data

        if(LinkedList.head == None):
            LinkedList.head = newNode
        else:
            LinkedList.tail.next = newNode
        LinkedList.tail = newNode
        LinkedList.length += 1
    
    def insertHead(self, data):
        
        newNode = ListNode()
        newNode.val = data
        
        if(LinkedList.head == None):
            LinkedList.head = newNode
        else:
            newNode.next = LinkedList.head
            LinkedList.head = newNode
        LinkedList.length += 1
    
    def insert(self,data, index):
        
        newNode = ListNode()
        newNode.val = data
        counter = 0
        
        if(LinkedList.head == None):
            LinkedList.head = newNode
        else:
            temp = LinkedList.head
            
            while(temp and counter < index):
                temp = temp.next
                counter += 1
                
            temp2 = temp.next
            temp.next = newNode
            newNode.next = temp2
        LinkedList.length += 1
            
    def remove(self, index):
        
        if(LinkedList.head == None):
            return -1
        else:
            prev = None
            curr = LinkedList.head
            counter = 0
            while(temp and counter < index):
                prev = curr
                curr = curr.next
                    
        
obj = LinkedList()
obj.append(10)
obj.append(20)
obj.append(30)
obj.insertHead(50)
obj.insertHead(60)
obj.insertHead(70)