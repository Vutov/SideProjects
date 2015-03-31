def palin3(word):
    ''' (str) -> bool

    Връща True или False според това дали word е palindrome или не.

    >>> palin3('racecar')
    True
    >>> palin3('book')
    False
    '''

    result = True
    
    for i in range(len(word)):
        if word[i] != word[-1 - i]:
            result = False

    return result

def palin2(word):
    ''' (str) -> bool

    Връща True или False според това дали word е palindrome или не.

    >>> palin2('racecar')
    True
    >>> palin2('book')
    False
    '''

    comp = ''

    for i in range(len(word) // 2):
        comp += (word[-1 - i])

    return word[:(len(word) // 2)] == comp

def palin1(word):
    ''' (str) -> bool

    Връща True или False според това дали word е palindrome или не.

    >>> palin1('racecar')
    True
    >>> palin1('book')
    False
    '''
    
    new_word = ''
    
    for i in range(len(word)):
         new_word += word[-1 -i]

    return new_word == word
