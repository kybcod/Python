result = 0
chi = 1081 #치킨의 수이자 쿠폰의 수


# 한마리당 쿠폰 한장 
# 10장 모으면(10마리 먹으면) 한 마리 무료 
# 서비스 치킨에도 쿠폰 발급
while chi >= 10:
    result += chi // 10 #현재쿠폰
    print('result =' ,result)
    
    #사용한 쿠폰 수 + 남은 쿠폰 수 (여태까지 시켜 먹은 치킨 수)
    chi = chi // 10 + chi % 10  
    print('chi =', chi)
print(result)