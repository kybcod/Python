common = [1, 2, 3, 4]	
answer = []
result = 0


#앞에서부터 3가지 숫자보고 등비인지 등차인지 알 수 있다.
one, two, three = common[:3]

#등차수열
if two - one == three - two:
    result = common[-1] + (two - one)

#등비수열
elif two // one == three // two:
    result = common
    [-1] * (two // one)

print(result)