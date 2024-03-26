s = "Buy 1 get 2 free"
n = [c for c in s if c.isdigit()][-1] 
print(n)

#리스트 축약
# new_list = [expression(i) for i in iterable if filter(i)]
# iterable : 새로운 리스트를 만들기 위한 재료
# expression(i) : iterable의 각 요소를 저장할 변수
