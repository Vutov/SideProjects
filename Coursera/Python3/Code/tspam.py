list = [1, 2, 3, 4, 5, 6, 7]

def tspamr(list):
    ''' (int) -> str

    Return pyramid of T's right sided

    >>>tspamr(list):
    T
    TT
    TTT
    TTTT
    TTTTT
    TTTTTT
    TTTTTTT
    '''
    
    for num in list:
        if num < 8:
            print ('T'*num)


def tspaml(list):
    ''' (int) -> str

    Return pyramid of T's left sided

    >>>tspaml(list):
          T
         TT
        TTT
       TTTT
      TTTTT
     TTTTTT
    TTTTTTT
    '''
    
    empty = " "

    for num in list:
        if num < 8:
            print (empty*(7-num) + 'T'*num)
