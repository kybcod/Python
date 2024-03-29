def two_sum_brute(the_list, target):
    index_list = []
    for i in range(0, len(the_list)):
        for j in range(i, lne(the_list)):
            if the_list[i] + the_list[j] == target:
                return [the_list[i], the_list[j]]
            
            
#딕셔너리 사용
def two_sum(a_list, target):
    a_dict = {}
    for index, n in enumerate(a_list):
        rem = target - n
        if rem in a_dict:
            return index, a_dict[rem]
        else:
            a_dict[n] = index
            
a_list = [-1,2,3,4,7]
print(two_sum(a_list, 7))
