# for루프 : 리스트의 각 요소를 하나씩 비교
# while 루프 : 정렬된 왼쪽 절반의 어느 위치에 숫자 삽입

list = [6,5,8,2]

def insertion_sort(list):
    for i in range(1, len(list)):
        value = list[i]
        
        while i > 0 and list[i-1] > value:
            list[i] = list[i-1]
            i = i-1
        
        list[i] = value
    
    return list

print(insertion_sort(list))


