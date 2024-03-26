#비트연산자로 짝수와 홀수인지 확인하기
# 홀수는 항상 1로 끝납니다.

def is_even(n):
    return not n & 1


# 2의 거듭제곱
def is_poewr(n):
    if n & (n-1) == 0:
        return True
    return False