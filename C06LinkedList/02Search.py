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
                
    def search(self, target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False
    

#1~30까지의 범위에서 무작위로 
# 숫자 20개의 링크드리스트를 
# 만든 다음 10을 탐색

import random

a_list = LinkedList()

for i in range(0,20):
    j = random.randint(1,30)
    a_list.append(j)
    print(j, end=" ")
    
print(a_list.search(10))