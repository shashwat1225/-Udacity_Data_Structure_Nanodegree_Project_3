def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    try:
        if number <0:
            output = "Can't square negative number"
            raise ValueError(output)
    except ValueError as error:
        print(error)
        return False

    if number is None:
        return None
    l = 1
    h = number
    old = l
    new = h
    while old != new:
        old = new
        sq = old*old
        if sq < number:
            l = old
        elif sq > number:
            h = old
        new = (l + h)//2
    return new
    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (1 == sqrt(1.5)) else "Fail")
print ("Pass" if  (False == sqrt(-1)) else "Fail")
