def binary_search(list, element):
    begin = 0
    end = len(lst) - 1

    while begin <= end:  # as long as 0 is less than length of list, then run this code
        mid_index = begin + (end - begin) // 2  # get remainder of items in list //2
        mid_value = lst[mid_index]  # set the value to the value returned above
        if mid_value == element:  # yeee got it
            return mid_index  # return the index position
        elif element < mid_value:  # but if the value is less than the value that means it goes to the left
            end = mid_index - 1  # this changes the ending position of the list to the item less than the previously returned value
        else:
            begin = mid_index + 1  # this changes the begining value to the list item mooore than the previously returned value
    return -1


lst = [4,8,5,15,16,23,42]
element = 15

print(binary_search(lst, element))
