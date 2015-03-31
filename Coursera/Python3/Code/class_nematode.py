class Nematode:
    ''' Information about Nematode'''

    def __init__(self, length, gender, age):
        ''' (Nematode, fload, str, int) -> NoneType

        Information about C. elegans, including a variable for the
        body length (in millimeters; they are about 1 mm in length),
        gender (either hermaphrodite or male), and age (in days).

        >>> nem = Nematode(1.2, 'male', 20) 
        >>> nem.length
        1.2
        >>> nem.gender
        'male'
        >>> nem.age
        20
        '''

        self.length = length
        self.gender = gender
        self.age = age

    def __str__(self):
        ''' (Nematode) -> str

        Return a human readable information for Nematode.

        >>> nem = Nematode(1.2, 'male', 20)
        >>> print(nem)
        C. elegans has 1.2 mm lenght, it is male and 20 days old.
        '''

        return '''C. elegans has {0} mm lenght, it is {1} and {2} days old.'''.format(
            self.length, self.gender, self.age)

    def __repr__(self):
        ''' (Nematode) -> str

        Return representation of the Nematode.

        >>> nem = Nematode(1.2, 'male', 20)
        >>> nem
        Nematode( '1.2', 'male', '20')
        '''

        return '''Nematode( '{0}', '{1}', '{2}')'''.format(
            self.length, self.gender, self.age)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
            
        
                
