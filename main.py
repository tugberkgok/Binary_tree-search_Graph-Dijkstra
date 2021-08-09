def binary_search(list,value):
    first_index = 0
    print(list)
    last_index=len(list)-1
    while first_index <= last_index:
        middle_index = (first_index+last_index)//2
        print(middle_index)
        middle_value=list[middle_index]
        print("Middle Value: {}".format(middle_value))
        if middle_value == value:
            return middle_value
        elif middle_value < value:
            first_index = middle_index
            print("New last index: {} ".format(last_index))
        elif middle_value > value:
            last_index = middle_index
            print("New First index : {}". format(first_index))

    None


L = [1,2,3,4,5,6,7,8,9]
P = 6
s = binary_search(L,P)
print("Value: {}" .format(s))

