#큰 수의 법칙
# 가장 큰 수를 K번 더하고 두번쨰로 큰 수를 한번더 더한다.

n,m,k = list(map(int, input().split()))
data = list(map(int, input().split()))

data.sort()
maxNum = data[n-1] #가장 큰 수
maxSecondNum = data[n-2]  # 두번째로 가장 큰 수

result = 0

while True:
    
    # 1. K번까지 가장 큰 수 더하기
    for i in range(k):
        if m == 0: break
        result += maxNum
        m -= 1
    
    # 2. K번 종료 시 두 번째 큰 수 더하기(한번)
    if m == 0: break
    result += maxSecondNum
    m -= 1

print(result)
    
    
#int (M/(K+1)) * K + ( M % (K+1) ) 
# 가장 큰 수가 더해지는 횟수
count = int(m/(k+1))*k
count += m % (k+1)


result1 = 0
result1 += (count) * maxNum #가장 큰 수 더하기
result1 += (m-count) * maxSecondNum # 두 번째로 큰 수 더하기

print(result1)
    
    

