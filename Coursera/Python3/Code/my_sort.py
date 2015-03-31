def my_sort(L):
    ''' (list of int) -> list of int

    Return sorted list of int.

    >>> my_sort([3, 5, 7, 1, 4])
    [1, 3, 4, 5, 7]
    >>> my_sort([1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> my_sort([])
    []
    >>> my_sort([1])
    [1]
    >>> my_sort([1, 1, 2, 5, 6, 1, 1, 2, 3])
    [1, 1, 1, 1, 2, 2, 3, 5, 6]
    '''

    a = len(L)
    new = 0
    new_lst = []
    
    for item in range(a):
        new = min(L)
        L.remove(new)
        new_lst.append(new)

    return new_lst

if __name__ == '__main__':
    import doctest
    doctest.testmod()
