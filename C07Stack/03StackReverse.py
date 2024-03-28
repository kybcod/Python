def reverse_string(a_string):
    stack = []
    string = ""
    for c in a_string:
        stack.append(c)
    
    for c in a_string:
        string += stack.pop()
    
    return string

print(reverse_string("Bieber"))

# 문자열 뒤집는 방법 
# 1. a_string[::-1]
# 2. ''.join(reversed('a_sting'))
# 3. 스택