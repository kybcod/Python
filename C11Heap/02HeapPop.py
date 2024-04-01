from heapq import heapify, heappop

a_list = ['R','C','T','H','E','D','L']
heapify(a_list)
print(a_list)

# heappop : 힙에서 가장 작은 요소 꺼내고 정렬
print("After poping")
heappop(a_list) 
print(a_list)

