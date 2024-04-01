# 로프 연결하는 최소 비용 찾기

from heapq import heapify, heappop, heappush

def find_min_cost(ropes):
    heapify(ropes) [2,4,5,8]
    cost = 0
    while len(ropes) > 1:
        #가장 작은 2개의 값
        sum = heappop(ropes) + heappop(ropes) 
        heappush(ropes, sum)
        cost += sum
    return cost

ropes = [5,4,2,8]
print(find_min_cost(ropes))