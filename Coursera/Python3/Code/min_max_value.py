def min_max_value(L, M):
    ''' (list of int, str) -> int

    Return the min or max value in the list, where L is the list
    and M is 'min' or 'max', depending on the callers needs.

    >>> min_max_value([1, 3, 7, 2, 5, 30], 'min')
    1
    >>> min_max_value([1, 3, 7, 2, 5, 30], 'max')
    30
    '''
    
    
    if M == 'min':
        minimum = min(L)
        return minimum
    
    elif M == 'max':
        maximum = max(L)
        return maximum

if __name__ == '__main__':
    import doctest
    doctest.testmod()
