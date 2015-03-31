def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int

    s1 and s2 are strings, and letter is a string of length 1.  Count how many
    times letter appears in s1 and in s2, and return the bigger of the two
    counts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''

    return max(s1.count(letter), s2.count(letter))
