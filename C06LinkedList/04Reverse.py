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
        
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return ' -> '.join(result)
                
                
    # 현재 노드가 이전 노드를 변수에 저장하고 
    # 현재 노드가 이전 노드를 가리키도록 바꾼다.
    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
        
        
# current: 현재 노드를 가리키는 포인터
# previous : 현재 노드의 이전 노드를 가리키는 포인터
# next: 현재 노드의 다음 노드를 임시로 저장하는 변수

a_list = LinkedList()
a_list.append(30)
a_list.append(20)
a_list.append(60)
a_list.append(80)
a_list.append(10)
print(a_list)

a_list.reverse_list()
print(a_list)