class Box:
    def __init__(self , data):
        self.data=data
        self.next=None
        
boxes = [Box(i) for i in range(51, 61)]

for i in range(len(boxes) - 1):
    boxes[i].next = boxes[i + 1]

def insertAtTail(head,ele):
    temp=Box(ele)
    if head == None:
        return temp
    tail = head
    
    while tail.next != None:
        tail= tail.next
    tail.next=temp
    return head

def insertAtBegining(head,ele):
    

def printLinkedlist(curr):
    while curr != None:
        print(curr.data)
        print(curr.next)
        curr=curr.next
        
printLinkedlist(boxes[0])



 