def different(a, b):
    ''' (int) -> bool

    Връща True ако a е различно от b и False ако са еднакви

    >>>different(2,2)
    False
    >>>different(2,3)
    True
    '''

    if a != b:
        return True
    else:
        return False
