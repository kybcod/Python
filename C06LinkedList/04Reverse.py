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
                
    def reverse_list(self):
        current = self.head
        pre = None
        while current:
            next = current.next
            current.next = pre
            pre = current
            current = next
        self.head = pre