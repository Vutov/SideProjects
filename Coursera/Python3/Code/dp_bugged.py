def double_preceding(values):
    """ (list of number) -> NoneType

    Replace each item in the list with twice the value of the
    Chapter 15. Testing and Debugging • 312
    report erratum • discuss
    preceding item, and replace the first item with 0.

    >>> L = [1, 2, 3]
    >>> double_preceding(L)
    >>> L
    [0, 2, 4]
    """

    if values != []:
        temp = values[0]
        values[0] = 0

    for i in range(1, len(values)):
        values[i] = 2 * temp
        temp = values[i]

def average(values):

    """ (list of number) -> number

    Return the average of the numbers in values. Some items in values are
    None, and they are not counted toward the average.

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """

    count = 0 # The number of values seen so far.
    total = 0 # The sum of the values seen so far.

    for value in values:
        if value is not None:
            total += value
            count += 1

    return total / count

import doctest
doctest.testmod()

