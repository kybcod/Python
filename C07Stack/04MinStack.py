
#최소값 찾기

# main, min 스택을 만들어 숫자들끼기 비교한 다음 
# min 스택에 넣어준다. 
# min 스택에 들어갈 때 맨 마지막 요소와 비교한 후 보다 작으면 들어간다.

class MinStack():
    def __init__(self):
        self.min = []
        self.main = []
    
    def push(self, n):
        if len(self.main) == 0:
            self.min.append(n)
        elif n <= self.min[-1]:
            self.min.append(n)
  
        #else 부분 없어도 됨 ?
        # self.min의 요소 수가 main과 동일하게 유지
        else:
            self.min.append(self.min[-1])

        self.main.append(n)
        
    def pop(self):
         self.min.pop()
         return self.main.pop()
    
    def get_min(self):
        return self.min[-1]
    
    
    
min_stack = MinStack()

min_stack.push(10)
print(min_stack.main)
print(min_stack.min)

min_stack.push(15)
print("main : "+ str(min_stack.main))
print("min : " + str(min_stack.min))

min_stack.push(5)
print("main : "+ str(min_stack.main))
print("min : " + str(min_stack.min))

min_stack.push(25)
print("main : "+ str(min_stack.main))
print("min : " + str(min_stack.min))

print(min_stack.get_min())

min_stack.pop()
print("main : "+ str(min_stack.main))
print("min : " + str(min_stack.min))