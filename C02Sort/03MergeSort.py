# 리스트를 계속 반으로 나눠 
# 요소가 한 개뿐인 리스트로만 남을 때 
# 순서대로 다시 함치는 재귀 정렬 알고리즘

def merge_sort(list):
    
    #리스트 -> 서브 리스트로 분할
    if len(list) > 1:
        mid = len(list) //2
        left_half = list[:mid]
        right_half = list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        
        
        #리스트 병합
        left_index = 0
        right_index = 0
        list_index = 0
        
        #왼쪽 리스트와 오른쪽 리스트에 요소가 남아있는 동안
        while left_index < len(left_half) and right_index < len(right_half):
            
             #왼쪽 리스트와 오른쪽 리스트 인덱스 앞에서 부터 비교
            if left_half[left_index] <= right_half[right_index]:
                list[list_index] = left_half[left_index]
                left_index += 1
            else:
                list[list_index] = right_half[right_index]
                right_index += 1
            
            list_index += 1
            
        # 남은 요소들을 결과 리스트에 복사
        # 왼,오 리스트 중 하나에만 요소가 남을 경우
        while left_index < len(left_half):
            list[list_index] = left_half[left_index]
            left_index += 1
            list_index += 1
            
        while right_index < len(right_half):
            list[list_index] = right_half[right_index]
            right_index += 1
            list_index += 1
        
    return list
            
            
list = [6,3,9,2]
print(merge_sort(list))


#파이썬에서 사용하고 있는 sorted함수, sort함수는 알고리즘은 Timsort
# Timsort는 삽입 정렬(Insertion Sort)과 병합 정렬(Merge Sort)을 결합