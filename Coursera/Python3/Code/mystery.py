def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result

def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements from L
    concatenated together, starting with indices 0 and 1, 2 and 3,
    and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        i = i + 2

    return compressed_list

def even_count(num1, num2):

    ''' (int) -> int

    Сума на четните числа в интервала [num1; num2).

    >>> even_count(2, 11)
    30
    >>> even_count(2, 10)
    20
    >>> even_count(1, 7)
    12
    '''

    count = 0
    num3 = num1 / 2
    
    if num1 / 2 == int(num3):
        for num in range(num1, num2, 2):
            count += num
    else:
        num4 = num1 + 1
        for num in range(num4, num2, 2):
            count += num

    return count
