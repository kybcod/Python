# 리스트에 중복 요소 반환

def return_dups(a_list):
    dups = []
    a_set = set()
    
    for item in a_list:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        
        if l1 == l2:
            dups.append(item)
            
    return dups

def return_notDups(a_list):
    dups = []
    a_set = set()
    
    for item in a_list:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        
        if l1 != l2:
            dups.append(item)
            
    return dups


a_list = ["apple","banana","orange","apple","kiwi"]
# print(return_dups(a_list)) #['apple']
print(return_notDups(a_list)) #['apple', 'banana', 'orange', 'kiwi']




