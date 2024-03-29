def count(a_string):
    a_dict = {}
    for char in a_string:
        if char in a_dict:
            a_dict[char] += 1 #key가 있으면 count++
        else:
            a_dict[char] = 1 #key가 없다면 value = 1
    print(a_dict)
    
count("hello")