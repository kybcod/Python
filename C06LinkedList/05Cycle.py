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
        
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next # 포인터 한번 이동
                fast = fast.next.next # 포인터 두번 이동
                
                # 두 노드가 동일한 노드를 가리키는지,
                # 둘이 만나면 사이클 존재
                if slow is fast:
                    return True
            except:
                return False