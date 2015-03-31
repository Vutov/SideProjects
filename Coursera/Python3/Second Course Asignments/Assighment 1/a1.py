def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """
    return (n - 1) // 50 + 1

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """

    result = ()
    gains = 0
    loses = 0
    
    for price in price_changes:
        if price > 0:
            gains += price
        elif price < 0:
            loses += price

    result = (gains, loses)

    return result


    
def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    
    if not 0 <= k <= len(L) // 2:
        return 'Invalid value for k, check precondition!'

    new_list = []

    for last in range(k):
        new_list.append(L[-k + last])

    for middle in range(k, len(L) - k):
        new_list.append(L[middle])

    for first in range(k):
        new_list.append(L[first])
        
    return new_list

if __name__ == '__main__':
    import doctest
    doctest.testmod()
