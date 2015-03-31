def repeat(s, n):
    """ (str, int) -> str

    Return s repeated n times; if n is negative, return the empty string.

    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    
    >>> repeat('no', -2)
    
    >>> repeat('yesnomaybe', 3)
    'yesnomaybeyesnomaybeyesnomaybe'
    """

    if n > 0:
        return s * n
    else:
        return

def total_length(s1, s2):
    """ (str, str) -> int

    Return the sum of the lengths of s1 and s2.

    >>> total_length('yes', 'no')
    5
    >>> total_length('yes', '')
    3
    >>> total_length('YES!!!!', 'Noooooo')
    14
    """

    return len(s1) + len(s2)
