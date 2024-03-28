class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
                
    def remove(self, target):
        if self.head == target:
            self.head = self.head.next
            return
        
        current = self.head
        previous = None
        while current:
            if current.data == target:
                #이전 노드의 포인터를 현재 노드의 다음 노드로 변경
                ppreviousre.next = current.next 
            previous = current 
            current = current.next