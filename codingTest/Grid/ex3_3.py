#숫자 카드 게임
# 카드 여러 장 중 가장 높은 숫자 카드 뽑는 게임
# 1. 뽑고자 하는 카드가 포함되어 있는 행 선택
# 2. 선택된 행에 초함된 카드들 중 가장 숫자가 낮은 카드 선택
# 3. 가장 높은 숫자의 카드를 뽑을 수 있도록 전략

#첫 번째 방법(min사용하기)
n,m = map(int, input().split())

result = 0

for i in range(n): #행만 반복
    data = list(map(int, input().split())) #행에 데이터 입력
    min_value = min(data) #현재 행 중 가장 작은 수 찾기
    result = max(result, min_value) #가장 작은 수 중 큰 수 찾기
    
print(result)


#두 번째 방법(2중 반복문)
for i in range(n):
    data = list(map(int, input().split()))
    
    min_value = 10001
    
    #현재 줄에서 가장 작은 수 찾기
    for a in data:
        min_value = min(min_value,a)
        
    # 각 행 중 작은 수 중에 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result)