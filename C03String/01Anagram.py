#애너그램 : 문자의 순서나 대소에 관계없이 똑같은 문자들로 구성된 두 문자열
def is_anaram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    if(sorted(s1) == sorted(s2)):
        return True
    else:
        return False
    
print(is_anaram('Car',"arc"))