# 피즈퍼즈 문제
# 1~100 숫자를 거치며 각각의 숫자가 나머지 연산을 통해 
# 3과 5의 공배수인지, 3의 배수인지(Fizz), 5의 배수인지(Buzz) 확인

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else: print(i, end=' ')
        
fizzbuzz(15)