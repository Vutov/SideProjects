def linear_search(L, V):

    none = -1
    
    for i in range(len(L)):
        if L[i] == V:
            none = i

    return none
