def move_zero(a_list):
    zero_ind = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_ind] = n
            if zero_ind != index:
                a_list[index] = 0
            zero_ind += 1
    return(a_list)

a_list = [8,0,3,0,12]
move_zero(a_list)
print(a_list)