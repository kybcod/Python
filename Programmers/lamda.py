#정수 n을 기준으로 n과 가까운 수 부터 정렬

numlist = [1, 2, 3, 4, 5, 6]	
n = 4
answer = []

print(sorted(numlist, key=lambda i: (abs(i-n), n-i)))

#sorted(, key) # key는 정렬 기준
# n과의 차이 절대값과 n과의 거리 기준으로 정렬