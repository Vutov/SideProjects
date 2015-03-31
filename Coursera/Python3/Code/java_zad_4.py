def java_zad_4(a, b):
    ''' (int, int) -> int

    Return how many numbers can be devided by 5 without leftovers
    in range between the 2 numbers provided.

    >>> java_zad_4(1, 11)
    2
    >>> java_zad_4(6, 2)
    1
    '''

    count = 0

    if a > b:
        for n in range(b, a):
            if n % 5 == 0:
                count += 1
        return count

    else:
        for n in range(a, b):
            if n % 5 == 0:
                count += 1
        return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
