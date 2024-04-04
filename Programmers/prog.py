polynomial = '3x + 7 + x'
answer = ''

xsum = 0
const = 0

for num in polynomial.split(" + "):
    if num.isdigit():
        const += int(num)
    elif 'x' in num:
        if num[:-1].isdigit():
            xsum += int(num[:-1])
        else: #1은 생략되므로 앞에 숫자가 없다면 +1
            xsum += 1
        
        
print(const)
print(xsum)