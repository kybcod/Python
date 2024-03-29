class Node:
    def __init__(self, data, next =None):
        self.data = data
        self.next = next
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = None
        
    #queue는 뒤에서 삽입
    def enqueue(self, item):
        self._size += 1
        node = Node(item)
        if self.rear is None:
            self.rear = node
            self.front = node
        else:
            self.rear.next = node
            self.rear = node
    
    #queue는 앞에서 삭제
    def dequeue(self):
        if self.front is None:
            raise IndexError("pop from empty queue")
        self._size -= 1
        temp = self.front
        self.front = self.front.next
        if self.front is None:
        
            self.rear = None
        return temp.data
    
    def size(self):
        return self._size
    
    
