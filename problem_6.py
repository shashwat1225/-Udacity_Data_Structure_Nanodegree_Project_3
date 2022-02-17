def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    maximum = ints[0]
    minimum = maximum
    for i in ints[1:]:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
    return minimum, maximum
    
    pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((5, 5) == get_min_max([5])) else "Fail")
print ("Pass" if ((-1, 1) == get_min_max([1, -1])) else "Fail")
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((0, 0) == get_min_max([0])) else "Fail") 
print("Pass" if (None is get_min_max([])) else "Fail")  
