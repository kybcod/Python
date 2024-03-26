
#소수 찾기
def is_prime_origin(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True



import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
    
def find_prime(n):
    return [i for i in range(2,n) if is_prime(i)]

print(find_prime(10))


# def is_prime(n):
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             print('x',end = ' ')
#     print(n, end=' ')