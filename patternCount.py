def getKmer( s, i, k ):
    """ Get the substring starting at position i of length k. """
    return s[i: i + k]


def patternCount( text, pattern ):
    count = 0
    lenPattern = len(pattern)
    lenDiff = len(text) - lenPattern
    for i in range(lenDiff + 1):
        if getKmer(text, i, lenPattern) == pattern:
            count += 1
    return count


def frequentWords( text, k ):
    """ Find the most frequent k-mers in the string text. """
    freqPatterns = set()
    limit = len(text) - k + 1
    count = [0] * limit
    for i in range( limit ):
        pattern = getKmer( text, i, k )
        count[i] = patternCount( text, pattern )
    maxCount = max(count)
    for i in range(limit):
        if count[i] == maxCount:
            freqPatterns.add( getKmer( text, i, k ))
    return freqPatterns


def hammingDistance( s1, s2 ):
    """ 
    Bioinformatics Algorithms, page 29 
    Compute the number of mismatches bewtween two equal-length strings.
    """
    strLen = len( s1 )
    count = 0
    for i in range( strLen ):
        if s1[i] != s2[i]:
            count += 1
    return count


def approxPatternCount( text, pattern, d ):
    count = 0
    limit = len( text ) - len( pattern ) + 1
    for i in range( limit ):
        patternPrime = getKmer( text, i, len( pattern ))
        if hammingDistance( pattern, patternPrime ) <= d:
            count += 1
    return count


def symbolToNumber( symbol ):
    """
    Maps the integers 0, 1, 2, 3 to A, C, G, and T respectively. 
    This implementation is used since I believe it will be faster
    than a list lookup. Page 43
    """
    if symbol == 'A': return 0
    if symbol == 'C': return 1    
    if symbol == 'G': return 2
    if symbol == 'T': return 3
    print( "Incorrect symbol " + symbol + " passed to symbolToNumber" )


def numberToSymbol( index ):
    """
    The inversse of symbolToNumber. Converts an integer 0-3 to A, C, G, T.
    Page 43
    """
    if index == 0: return 'A'
    if index == 1: return 'C'
    if index == 2: return 'G'
    if index == 3: return 'T'
    print( "Incorrect index " + str(index) + " passed to numberToSymbol" )



def patternToNumber( pattern ):
    """ Page 43 """
    if len( pattern ) == 0:
        return 0
    symbol = pattern[-1]
    prefix = pattern[0:-1]
    return 4 * patternToNumber( prefix ) + symbolToNumber( symbol )


def numberToPattern( index, k ):
    """ Page 44 """
    if k == 1:
        return numberToSymbol( index )
    prefixIndex = index // 4
    r = index % 4
    symbol = numberToSymbol( r )
    prefixPattern = numberToPattern( prefixIndex, k - 1 )
    return prefixPattern + symbol


def findFreqWordsBySorting( text, k ):
    """ Page 45 """
    frequentPatterns = set()
    limit = len( text ) - k + 1
    index = [0] * limit
    count = [0] * limit
    for i in range( limit ):
        pattern = getKmer( text, i, k )
        index[i] = patternToNumber( pattern )
        count[i] = 1
    sortedIndex = sorted( index )
    for i in range( 1, limit ):
        if sortedIndex[i] == sortedIndex[i - 1]:
            count[i] = count[i - 1] + 1
    maxCount = max( count )
    for i in range( limit ):
        if count[i] == maxCount:
            pattern = numberToPattern( sortedIndex[i], k )
            frequentPatterns.add( pattern )
    return frequentPatterns


def computingFrequencies( text, k ):
    limit = 4 ** k
    frequencyArray = [0] * limit
    for i in range( len(text) - k + 1):
        pattern = getKmer( text, i, k )
        j = patternToNumber( pattern )
        frequencyArray[ j ] += 1
    return frequencyArray 
        


def clumpFinding( genome, k, L, t ):
    frequentPatterns = set()
    limit = 4 ** k
    clump = [0] * limit
    for i in range( len(genome) - L + 1 ):
        text = genome[ i: i + L ]
        frequencyArray = computingFrequencies( text, k )
        for index in range( limit ):
            if frequencyArray( index ) >= t:
                clump[ index ] = 1
    for i in range( limit ):
        if clump[i] == 1:
            pattern = numberToPattern( i, k )
            frequentPatterns.add( pattern )
    return frequentPatterns


if __name__ == '__main__':
    f = frequentWords( 'ACGTCGATAT', 2)
    print(f)
    g = computingFrequencies( 'ACGTCGATATCC', 2)
    print(g)
