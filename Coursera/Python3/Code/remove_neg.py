def remove_neg(num_list):
    """ (list of number) -> list of number

    Remove the negative numbers from the list num_list and return the new list.

    >>> remove_neg([1, 2, 3, -3, 6, -1, -3, 1])
    [1, 2, 3, 6, 1]
    >>> list = [ 1, -3, 4, -5, 6, 7, -8]
    >>> remove_neg(list)
    [1, 4, 6, 7]
    """
    
    for item in num_list:
        if item < 0:
            num_list.remove(item)
            while num_list.count(item)!=0:
                num_list.remove(item)
    return num_list
