def complement(strain):
    ''' (str) -> str

    Return the complemet of a strain

    Precondition:
    Strain must be made of As, Ts, Gs and Cs

    >>> complement('ATGC')
    'TACG'
    >>> complement ('AATTGCCGT')
    'TTAACGGCA'
    '''

    for ch in strain:
        if ch not in 'A,T,G,C':
            print('Error, check the preconditions. Now allowed symbol:', ch)

    
    new_strain = ''
    
    for char in strain:
        if char == 'A' :
            new_strain += 'T'
        elif char == 'T':
            new_strain += 'A'
        elif char == 'G':
            new_strain += 'C'
        else:
            new_strain += 'G'

    return new_strain
##    print ('The complement of', strain, 'is', new_strain,'.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
