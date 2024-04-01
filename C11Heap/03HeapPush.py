from heapq import heapify, heappop, heappush

a_list = ['D','E','L','H','R','T']
heapify(a_list)
heappush(a_list,'A')

while len(a_list)>0:
    print(heappop(a_list))
    