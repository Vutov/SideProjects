def find_dups(list):
    ''' (list of int) -> set of int

    Returns a set of integers that occur two or more times in the list.

    >>> find_dups([1, 2, 3, 4, 5, 1, 2, 1])
    (1, 2, 1)
    >>> find_dups([4, 5, 7, 1, 3, 5, 3])
    (5, 3)
    '''

    dups = set()
    uniq = []
    for item in list:
        if item not in uniq:
            uniq.append(item)
        else:
            dups.add(item)

    return dups

def mating_pairs(males, females):
    ''' (two sets) -> set of tuples

    Returns a set of pairs; each pair is a tuple containing one male and
    one female.
    
    Predconditions:
    lenght of males = size of females

    >>> mating_pairs(set([143, 144, 145]),set([133, 134, 135]))
    ((143, 133), (144, 134), (145, 135))
    >>> mating_pairs(set('a', 'b'),set('c', 'd'))
    (('a', 'c')('b', 'd'))
    '''

##    result = tuple()
##
##    for animal in males:
##        males.pop()

def pdb(x):
    ''' (file) -> set

    Return set of all author names found in a file.

    '''

    file = 'd://desktop//13.txt'

    name = set()

    with open(file, 'r') as junk_data:
        for i in range(1000):
            data = junk_data.readline().lower()
            if data.startswith('author'):
                name.add(data)
    if 'author' in name:
        name.remove('author')
    print (name)

def count_values(dict):
    ''' (dict) -> int

    Return the number of distinct values dictionary contains.

    >>> count_values({'red': 1, 'green': 1, 'blue': 2})
    2
    >>> count_values({'s': 3, 'g': 3})
    1
    '''

    count = set()
    
    for key in dict:
        value = dict[key]
        count.add(value)
        
    return len(count)

def exp(dict):
    ''' (dict) -> int

    Return the particle that is least likely to be observed.

    >>> exp({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14})
    'meson'
    '''

##    values = []
##    for key in dict:
##        value = dict[key]
##        values.append(value)
##
##    the_one = min(values)
####    print(the_one)
##    return dict[the_one]
    vis = 1
    kis = ''
    for key, value in dict.items():
        if value < vis:
            vis = value
            kis = key
    return kis

def count_duplicates(dict):
    ''' (dict) -> int

    Takes a dictionary as an argument and returns the number of values that appear
    two or more times.

    >>> count_duplicates({1: 3, 2: 3, 4: 4, 5: 5, 6: 4})
    2
    '''

    count = 0
    lst = []
    for key in dict:
        value = dict[key]
        if value not in lst:
            lst.append(value)
        else:
            count += 1

    return count

def is_balanced(dict):
    ''' (dict) -> bool

    Return True if the color is balanced

    Precondition:
    dict must have only 3 keys - 'R', 'G', 'B'

    >>> is_balanced({'R': 1.0, 'G': 1.0, 'B': 1.0})
    True
    >>> is_balanced({'R': 0.9, 'G': 1.0, 'B': 1.0})
    False
    '''

    balanced = True

    for key in dict:
        if dict[key] != 1:
            balanced = False
            
    return balanced

def dict_intersect(dict1, dict2):
    ''' (dicts) -> dict

    Returns a dictionary that contains only the key/value pairs found in
    both of the original dictionaries.

    Precondition:
    if there is the same key in dict2 as in dict1, in the new dictionary will be only dict2's
    with it's value
    
    >>> dict_intersect({1: 2, 2: 3},{3: 4, 4: 5})
    {1: 2, 2: 3, 3: 4, 4: 5}
    >>> dict_intersect({1: 2, 2: 3},{3: 4, 2: 5})
    {1: 2, 2: 5, 3: 4}
    '''

    new_dict = dict1

    for key in dict2:
        new_dict[key] = dict2[key]

    return new_dict
    
def db_headings(dict):
    ''' (dict of dicts) -> set of keys

    Return the set of keys used in any of the inner dictionaries.

    >>> db_headings({
    'jgoodall' : {'surname' : 'Goodall',
    'forename' : 'Jane',
    'born' : 1934,
    'died' : None,
    'notes' : 'primate researcher',
    'author' : ['In the Shadow of Man',
    'The Chimpanzees of Gombe']},
    'rfranklin' : {'surname' : 'Franklin',
    'forename' : 'Rosalind',
    'born' : 1920,
    'died' : 1957,
    'notes' : 'contributed to discovery of DNA'},
    'rcarson' : {'surname' : 'Carson',
    'forename' : 'Rachel',
    'born' : 1907,
    'died' : 1964,
    'notes' : 'raised awareness of effects of DDT',
    'author' : ['Silent Spring']}
    })
    ('author', 'forename', 'surname', 'notes', 'born', 'died')
    '''

    st = set()

    for name in dict:
        for key in dict[name]:
            st.add(key)
    return st

def db_consistent(dict):
    ''' (dict of dicts) -> bool

    Returns True if and only if every one of the inner dictionaries has exactly the same keys.

    >>> db_consistent({
    'jgoodall' : {'surname' : 'Goodall',
    'forename' : 'Jane',
    'born' : 1934,
    'died' : None,
    'notes' : 'primate researcher',
    'author' : ['In the Shadow of Man',
    'The Chimpanzees of Gombe']},
    'rfranklin' : {'surname' : 'Franklin',
    'forename' : 'Rosalind',
    'born' : 1920,
    'died' : 1957,
    'notes' : 'contributed to discovery of DNA'},
    'rcarson' : {'surname' : 'Carson',
    'forename' : 'Rachel',
    'born' : 1907,
    'died' : 1964,
    'notes' : 'raised awareness of effects of DDT',
    'author' : ['Silent Spring']}
    })
    False
    '''
    
    result = True # първоначално условие
    dkt = {}
    count = 0
    
    for name in dict:
        for key in dict[name]: # луп за ключ в ключа
            if key in dkt:
                dkt[key] = dkt[key] + 1 # нов речник съдържащ броя ключове в ключа
            else:
                dkt[key] = 1
                
        for new_key, value in dkt.items(): # проверява дали всички стойности са равни на последния
# размер на ключовете в ключа
            count = value
            if value != len(dict[name][key]):
                result = False
    
    return result            
##            if len(dict[name][key]) != len(dict[name][
