def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)

##    if len(dna1) > len(dna2):
##        return True
##    else:
##        return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    cnucleotides = 0

    for char in dna:
        if char in nucleotide:
            cnucleotides = cnucleotides + 1

    return cnucleotides

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1


def is_valid_sequence(dnas):
    ''' (str) -> bool

    Return True if and only if the DNA sequence is valid (that is, it contains no characters other than 'A', 'T', 'C' and 'G').

    >>> is_valid_sequence('ATTC')
    Ttue
    >>> is_valid_sequence('ATG')
    True
    >>> is_valid_sequence('ATat')
    False
    >>> is_valid_sequence('cgat')
    False
    '''

    c = count_nucleotides(dnas,'a,t,c,g')

    return c == 0

##    for char in dnas:
##        if char not in 'ATCG':
##            return False
##    return True

def insert_sequence(seq1, seq2, index):
    ''' (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.

    >>>insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>>insert_sequence('ATTC','GCA',4)
    'ATTCGCA'
    >>>insert_sequence('ATG','CA',1)
    'ACATG'
    '''

    return seq1[:index] + seq2 + seq1[index:]

def get_complement(nucleotide):
    ''' (str) -> str

    Return the nucleotide's complement.

    >>>get_complement('A')
    'T'
    >>>get_complement('T')
    'A'
    >>>get_complement('C')
    'G'
    >>>get_complement('G')
    'C'
    '''

    if nucleotide is 'A':
        return 'T'
    elif nucleotide is 'T':
        return 'A'
    elif nucleotide is 'C':
        return 'G'
    elif nucleotide is 'G':
        return 'C'
    else:
        return 'Error, not A, T, C or G'

def get_complementary_sequence(sequence):
    ''' (srt) -> srt

    Return the DNA sequence that is complementary to the given DNA sequence.
    
    >>>get_complementary_sequence('ACGTACG')
    'TGCATGC'
    >>>get_complementary_sequence('TGCAGCT')
    'ACGTCGA'
    '''
    
    cs = ''
    
    for char in sequence:
        cs = cs + get_complement(char)
    return cs
    
    
