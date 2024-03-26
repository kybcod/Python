def linear_search(list, n):
    for i in list:
        if i == n:
            return True
    return False

list = [1,67,77,34,7]
print(linear_search(list, 67)) #True


#한줄
print(67 in list)
print('a' in 'apple')