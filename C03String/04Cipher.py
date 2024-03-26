# Cipher : 암호화나 복호화에 사용되는 알고리즘 - 나눗셈 연산 중요

#a_string : 암호화할 문자열, key : 각 문자를 밀어낼 숫자

import string

def cipher(a_string, key):
    uppercase = string.ascii_uppercase #'ABCD...'
    lowercase = string.ascii_lowercase #'abcd...'
    
    encrypt = ''
    
    for c in a_string:
        
        if c in uppercase:
            new = (uppercase.index(c)+ key) % 26 #숫자
            encrypt += uppercase[new] #알파벳
        
        elif c in lowercase:
            new + (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        
        else:
            encrypt += c
    
    return encrypt

print(cipher("SEIDKFJ", 5))