class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data) #head가 없으면 새로운 노드가 head
            return
        
        #헤드가 이미 있다면
        current = self.head
        
        #마지막 노드 찾기(다음 노드가 없을 때까지 반복)
        while current.next:
            current = current.next
            
        #마지막 노드에 새로운 데이터 추가
        current.next = Node(data)
                
    #__str__ 메서드가 있는 객체를 출력할 때 사용            
    def __str__(self):
        node = self.head
    
        while node is not None:
            print(node.data)
            node = node.next
    
        return "end"


a_list = LinkedList()
a_list.append("Tuesday")
a_list.append("Wednesday")
print(a_list)


#내장되어 있는 링크드 리스트 : deque
from collections import deque

d= deque()
d.append("Harry")
d.append("Potter")

for item in d:
    print(item)