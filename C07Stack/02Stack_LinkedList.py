class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head # 새 노드의 다음 요소에 기존 헤드 값 할당
            self.head = node # 새 노드를 헤드로 만듬
        
        
    def pop(self):
        if self.head is None:
            raise IndexError('pop from empty stack')
        poppednode = self.head #첫번째 요소 제거를 위해 변수에 저장
        self.head = self.head.next #첫번째 요소 제거하기 떄문에 다음 첫번째 요소를 정해줌
        return poppednode.data # 첫번째 요소 제거
    
    
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

for i in range(3):
    print(stack.pop())