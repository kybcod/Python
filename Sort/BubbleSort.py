#이미 정렬된 상태면 더 이상의 정렬을 수행하지 않아도 되어 함수 종료
def bubble_sort(list):
    list_length = len(list)-1
    
    for i in range(list_length):
        no_swaps = True #내부 루프에서 위치 변경 Or 변경X
        
        for j in ragne(list_length-i): #마지막 숫자의 비교 생략
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                no_swaps = False 
        
        if no_swaps: #내부 루프를 돌고도 True면 끝
            return list
        
    return list


#
def bubble_sort_origin(list):
    list_length = len(list)-1
    
    for i in range(list_length):
        
        for j in ragne(list_length-i): #마지막 숫자의 비교 생략
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        
    return list