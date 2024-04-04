arr = [[80, 70], [90, 50], [40, 70], [50, 80]]
arr2 = ['false', 'true', 'true', 'true', 'true', 'false', 'false']
str = 'aBcDeFg'
answer = []
rank = []
result = 0


for i in arr:
    print(i)
    total = sum(i)/len(i)
    answer.append(total)
print(answer)

for i in sorted(answer, reverse=True):
    rank.append(answer.index(i)+1)

print(rank)