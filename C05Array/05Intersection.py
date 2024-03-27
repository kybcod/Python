def return_inter_list(list1, list2):
    dup = []
    for v in list1:
        if v in list2 and v not in dup:
            dup.append(v)
    return dup
#[v for v in list1 if v in list2]
     

def return_inter_set(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))


list1 = [2,3,4,56,3,4,36]
list2 = [2,3,6,32,5,4,3,1]
print(return_inter_list(list1, list2))
print(return_inter_set(list1, list2))



