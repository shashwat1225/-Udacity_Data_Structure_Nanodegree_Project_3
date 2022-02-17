def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    left_index = 0
    middle_index = len(input_list)-1
    right_index = middle_index
    while True:
        left = input_list[left_index]
        right = input_list[right_index]
        middle_index = (left_index + right_index) // 2
        mid = input_list[middle_index]
        if number == mid:
            return middle_index
        elif number == right:
            return right_index
        elif left_index == middle_index:
            return -1
        elif left < mid :
            if number >= left and number <= mid:
                right_index = middle_index 
            else:
                left_index = middle_index + 1
        elif mid < right:
            if number >= mid and number <= right:
                left_index = middle_index + 1
            else:
                right_index = middle_index
    pass

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[],1])
test_function([[2,1],7])
