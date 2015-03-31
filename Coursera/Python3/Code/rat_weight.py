def rat_weight(rat_rate):
    ''' (int) -> int

    Return the number of weeks needed for the weight of the rat to become 25 percent heavier than it was. originally.

    Preconditions:
    rat_rate is constant and > 0
    
    >>> rat_weight(5)
    5
    >>> rat_weight(1)
    25
    '''
    
    weight = 0
    count = 0
    
    while weight < 25:
        weight += rat_rate
        count += 1

    return count

def rat_race(rat_rate1, rat_rate2):
    ''' (int) -> int

    Return the number of weeks needed for the first rat to be 10 percent heavier than the second.

    Preconditions:
    Both rats have the same initial weight.
    rat_rate1 > rat_rate2
    rat_rate1, rat_rate2 = constant and > 0

    >>> rat_race(2, 1)
    10
    >>> rat_race(8, 1)
    2
    '''

    rat_weight1 = 0
    rat_weight2 = 0
    count = 0
    
    while rat_weight1 < rat_weight2 + 10:
        rat_weight1 += rat_rate1
        rat_weight2 += rat_rate2
        count += 1

    return count
        
