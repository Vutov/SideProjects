if __name__ == '__main__':
    from class_country import Country
    
class Continent:
    '''Information about Continent.'''

    def __init__(self, name, countries):
        ''' (Continent, name, list of Country objects) -> NoneType

        Represent a continet with a name and list of countries.

        >>> namerica = Continent('North America', ['USA', 'Canada'])
        >>> namerica.name
        'North America'
        >>> namerica.countries
        ['USA', 'Canada']
        '''

        self.name = name
        self.countries = countries
    
    def __str__(self):
        ''' (Continent) -> str

        Return a human readable information about the Continent.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> mexico = Country('Mexico', 112336538, 1943950)
        >>> countries = [canada, usa, mexico]
        >>> north_america = Continent('North America', countries)
        >>> print(north_america)
        North America
        Canada has a population of 34482779 and is 9984670 square km.
        United States of America has a population of 313914040 and is 9826675 square km.
        Mexico has a population of 112336538 and is 1943950 square km.
        '''

        res = self.name
        
        for country in self.countries:
            res = res + '\n' + str(country)

        return res
        
    def total_population(self):
        ''' (Continent) -> int

        Return the total population of the Continent.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> mexico = Country('Mexico', 112336538, 1943950)
        >>> countries = [canada, usa, mexico]
        >>> north_america = Continent('North America', countries)
        >>> north_america.total_population()
        460733357
        '''

        total = 0
        
        for country in self.countries:
            total += country.population
            
        return total
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
