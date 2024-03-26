
# # 출석 번호를 n번 무작위로 불렀을 때, 
# # 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

# n = int(input())
# a = list(map(int, input().split()))

# # 1부터 23까지의 빈도를 기록하는 리스트 생성 및 초기화
# frequency = [0] * 23  

# for i in a:
#     frequency[i - 1] += 1 #번호 1은 인덱스 0, 번호 n은 인덱스 n-1

# for freq in frequency:
#     print(freq, end=' ')

# #인덱스 9~0
# for i in range(n-1, -1, -1):
#      print(a[i], end =' ')
    
    
 
# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
# n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
d = [[0 for j in range(20)] for i in range(20)]
print(d)





