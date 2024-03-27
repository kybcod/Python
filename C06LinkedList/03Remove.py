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
        pre = None
        while current:
            if current.data == target:
                pre.next = current.next
            pre = current
            current = current.next