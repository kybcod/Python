import random

#2번
# date1 = random.randrange(4,29)
# print("오프라인 스터디 모임 날짜는 매월 {0}일로 선정되었습니다.".format(date1))

#3번
# url = "http://naver.com"
# my_str = url.replace("http://","")
# my_str = my_str[:my_str.index('.')]
# print("생성되 비밀번호 : {0}".format(my_str[:3]+str(len(my_str))+str(url.count('e'))+"!"))
# print(my_str)


#4번
# users = list(range(1,21)) #1~20 랜덤
# print(users)

# random.shuffle(users)
# print(users)

# winners = random.sample(users,4)

# print("---당첨자 발표---")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("축하합니다~")


#5번
# cnt = 0
# for i in range(1,51):
#     time = random.randint(5,50)
#     if 5<=time<=15:
#         print("[O] {0}번쨰 손님 (소요시간 : {1}분)".format(i,time))
#         cnt +=  1
#     else:
#         print("[ ] {0}번쨰 손님 (소요시간 : {1}분)".format(i,time))
# print("총 손님 수 : {0}".format(cnt))


#6번
# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#          return height * height * 21
    
# height = 175
# gender = "남자"
# weight = round(std_weight(height/100, gender),2)

# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(175, "남자", round(std_weight(height/100, gender),2)))
# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))

#리스트 컴프리헨션
a = [1,2,3,4,5]
rem = {3,5}

result = [i for i in a if i not in rem]
print(result)

re = []
for i in a:
    if i not in rem:
        re.append(i)

print(re)

#람다
def add(a,b): return a+b
print(add(2,3)) #5
print((lambda a,b:a+b)(2,3)) #5


#여러 개의 데이터를 입력받을 때 데이터가 공백으로 구분되는 경우
#n = int(input())

#각 데이터를 공백으로 구분하여 입력
#data = list(map(int, input().split(" "))) 
#map(int,...) : 문자열 정수로 변환, 
# input().split() : input함수 호출하여 사용자가 공백으로 숫자를 주어야 한다.

#print(data)

#m,k,p = map(int, input().split())
#print(m, k, p)

result = sum([1,2,3,4,5]) #15
result = min(2,3,4,5) #2
result = eval("(3+5)*7") #56
result = sorted([9,1,8,5,4]) #오름차순 정렬
result = sorted([9,1,8,5,4], reverse=True) #내림차순 정렬
result = sorted([('홍길동',35),('이순신',75),('아무개',50)], key = lambda x: x[0],reverse=True) #인덱스 0,1 : 이름,나이

print(result)

from itertools import combinations #조합 중복X
from itertools import product #순열과 비슷
from itertools import permutations #순열
from itertools import combinations_with_replacement #조합 중복O


data = ['A','B','C']
result = list(permutations(data,3)) #모든 순열 구하기
result = list(combinations(data,2)) #data 중 2개 뽑아 순서상관없이, 중복X
result = list(product(data, repeat = 2)) #2개를 뽑는 모든 순열(중복 허용)
result = list(combinations_with_replacement(data, 2)) #2개를 뽑아 순서고려X 중복 허용

import math

#소수 판별 함수
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False #소수아님
    return True

print(is_prime_number(7))

#시간 복잡도 더 좋다.
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False #소수아님
    return True

print(is_prime_number(7))

#에라토스테네스
# 2부터 N까지 모든 자연수 나열 
# 남은 수 중 아직 처리하지 않은 가장 작은 수 i 찾기  
# 남은 수 중 i배수 모두 제거(i 제외) 

n = 10
array = [True for i in range(n+1)] #모든 수 소수(True)인 것처럼 초기화

for i in range(2, int(math.sqrt(n))+1): #2~n제곱근
    if array[i] == True: #i는 소수
        #i를 제외한 모든 배수 지우기
        j = 2 
        while i*j <= n:
            array[i*j] = False
            j += 1
    
for i in range(2, n+1):
    if array[i]:
        print(i,end=' ')
        