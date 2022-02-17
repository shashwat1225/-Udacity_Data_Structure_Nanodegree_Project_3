def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    size = len(input_list)
    if size <= 1:
        return [-1,-1]
    frequency = [0]*10
    for i in input_list:
        frequency[i] += 1
    arraya = []
    arrayb = []
    count = 1
    if size %2 != 0:
        count = 2
    for i in range(9,-1,-1):
        while frequency[i]:
            if count:
                arraya.append(str(i))
                count -= 1
            else:
                count += 1
                arrayb.append(str(i))
            frequency[i]-=1
    return [int(''.join(arraya)), int(''.join(arrayb))]
    pass

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_function([[], [-1, -1]])
test_function([[0], [-1, -1]])
test_function([[0, 0], [0, 0]])
test_function([[1, 1, 1, 3, 5, 6], [631, 511]])
