#라이브러리 사용X
def binary_search(list,n):
    first = 0
    last = len(list)-1
    while last >= first:
        mid = (first+last)//2
        if list[mid]==n:
            return True
        else:
            if n < list[mid]: #찾는 값이 중앙값보다 작으면 
                last = mid - 1 #중앙값보다 큰 절반을 버림
            else:
                first = mid + 1 #중앙값보다 작은 절반을 버림
    return False
    
    
list = [9,3,6,1]
print(binary_search(list,2))

#bisect 라이브러리 사용
from bisect import bisect_left

def binary_search_bisect(an_iterable, target):
    
    #특정 요소의 삽입 지점이나 삽입 될 지점, 
    #해당 요소의 왼쪽(작은 쪽) 인덱스를 반환
    index = bisect_left(an_iterable, target) 
    
    if index <= len(an_iterable) and an_iterable[index] == target:
        return True
    return False

print(binary_search_bisect(list, 2))


#문자 탐색
def binary_search_char(list_char, target):
    left = 0
    right = len(list_char-1)
    
    while left <= right:
        mid = (left+right)//2
        mid_char = list[mid]
        
        if ord(mid_char) == target:
            return True
        elif ord(mid_char) < target:
            left = mid + 1
        else:
            right = mid -1
    return False

list_char = "afeijiaoejgkjeogi"
print(binary_search_char, ord('k'))
