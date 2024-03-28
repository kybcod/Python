
#괄호 검사(스택에 아무것도 없어야 성공(True))
def check_parentheses(a_string):
    stack = []
    for c in a_string:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0: 
                return False
            else:
                stack.pop()
    
    # 스택에 남은 왼쪽 괄호가 있는지 확인
    return len(stack) == 0

print(check_parentheses(")()()("))  #False

# 리스트의 append(), pop()은 스택의 push(), pop()과 같은 역할
