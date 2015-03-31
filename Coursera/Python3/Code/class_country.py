class Country:
    ''' Information about a country'''

    def __init__(self, name, popu, area):
        ''' (Country, name, population, area) -> NonType

        The name of the country is name, its population is popu
        and its area is area.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> canada.name
        'Canada'
        >>> canada.population
        34482779
        >>> canada.area
        9984670
        '''

        self.name = name
        self.population = popu
        self.area = area

    def __str__(self):
        ''' (Country) -> str

        Retrun human readable information about the country.

        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> print(usa)
        United States of America has a population of 313914040 and is 9826675 square km.
        '''

        return '''{0} has a population of {1} and is {2} square km.'''.format(
            self.name, self.population, self.area)

    def __repr__(self):
        ''' (Country) -> str

        Return a string representation of Country.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> canada
        Country('Canada', 34482779, 9984670)
        '''

        return '''Country('{0}', {1}, {2})'''.format(
            self.name, self.population, self.area)
    
    def is_larger(self, other):
        ''' (Country, Country) -> bool

        Retrun True iff self's area is larger than the other's.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> canada.is_larger(usa)
        True
        '''

        return self.area > other.area

    def population_density(self):
        ''' (Country) -> float

        Return the density of the Country (people per square km).

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> canada.population_density()
        3.4535722262227995
        '''

        return self.population / self.area

if __name__ == '__main__':
    import doctest
    doctest.testmod()
