# 최대공약수
def gcf(i1, i2):
    
    if i1 < 0 and i2 < 0: 
        raise ValueError("Numbers must be positive.")
    
    # 경계조건 : 0을 처리하지 못하는 경우
    if i1 == 0: return i2
    if i2 == 0: return i1
    
    if i1 > i2:
        smaller = i2
    else:
        smaller = i1
    
    for divisor in range(1, smaller+1):
        if (i1 % divisor == 0) and (i2 % divisor == 0):
            gcf = divisor

    return gcf

print(gcf(-20,12))
        
        