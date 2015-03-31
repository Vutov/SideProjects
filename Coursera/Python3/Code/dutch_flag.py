def dutch_flag(L):
    ''' (list of str) -> list of str

    Return the list of str in order of the dutch flag.
    
    >>> dutch_flag(['green', 'blue', 'blue', 'red', 'green', 'blue'])
    ['red', 'green', 'green', 'blue', 'blue', 'blue']
    '''

    dutch_fla = []
    red = []
    blue = []
    green = []
    
    for char in L:
        if char == 'red':
            red.append(char)
        elif char == 'green':
            green.append(char)
        elif char == 'blue':
            blue.append(char)
        else:
            raise AssertionError
        
    dutch_fla.extend(red)
    dutch_fla.extend(green)
    dutch_fla.extend(blue)
    
    return dutch_fla

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import cProfile
    cProfile.run('')
        
