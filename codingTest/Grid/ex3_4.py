# 1이 될 때까지
# 1. N이 K로 나누어지지 않으면 N에서 1을 뺸다.
# 2. N을 K로 나눈다.

n,k = map(int, input().split())
count = 0

# n이 k이상이면 k로 나누기
while n >= k:
    
    #n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n % k != 0:
        n -= 1
        count += 1
    
    #n이 k로 나누어 떨어지면 
    n//=k
    count += 1

while n > 1:
    n-=1
    count += 1
    
print(count)

result = 0
while True:
    #(N==K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n-target)
    n = target
    
    #N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    
    #K로 나누기
    result += 1
    n //= k
    
#마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)


     
#나누어 떨어지기 위해서 
