# 그리디
# 500, 100, 50, 10원
# 손님에게 거슬러 줘야 할 동전의 최소 개수

n = 1260
count = 0

coin = [500,100,50,10]
for c in coin:
    count += n // c
    n %= c

print(count)