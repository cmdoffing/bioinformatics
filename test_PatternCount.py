import unittest
from patternCount import *

class TestPatternCount( unittest.TestCase ):
    def testPatternCount(self):
        text = "ACGTTCG"
        pattern = "CG"
        self.assertEqual( patternCount( text, pattern ), 2 )
    def testPatternCountT(self):
        text = "ACGTTCG"
        pattern = "T"
        self.assertEqual( patternCount( text, pattern ), 2 )
    def testPatternCountG(self):
        text = "ACGTTCG"
        pattern = "G"
        self.assertEqual( patternCount( text, pattern ), 2 )

class TestFrequentWords( unittest.TestCase ):
    def test1_mer(self):
        self.assertEqual( frequentWords('ACGTCGATAT', 1), {'A', 'T'})
    def test2_mer(self):
        self.assertEqual( frequentWords('ACGTCGATAT', 2), {'AT', 'CG'})
    def test3_mer(self):
        self.assertEqual( frequentWords('ACGTCGATAT', 3),
             {'CGA', 'GTC', 'GAT', 'ACG', 'TAT', 'ATA', 'TCG', 'CGT'})

class TestHamming( unittest.TestCase ):
    def test_hamming1(self):
        self.assertEqual( hammingDistance('ACGTCG', 'CCGGAG'), 3)
    def test_hamming2(self):
        self.assertEqual( hammingDistance('ACGTCG', 'ACGTCG'), 0)
 
class TestApproxPatternCount( unittest.TestCase ):
    def testApproxPatternCount1(self):
        text = "ACGTTCG"
        pattern = "CCG"
        self.assertEqual( approxPatternCount( text, pattern, 1 ), 2 )
    def testApproxPatternCount2(self):
        text = "ACGTTCGACGTTCGACGTTCGACGTTCG"
        pattern = "AGTTA"
        self.assertEqual( approxPatternCount( text, pattern, 2 ), 4 )

class TestSymbolToNumber( unittest.TestCase ):
    def test_SymbolToNumber0(self):
        self.assertEqual( symbolToNumber('A'), 0)
    def test_SymbolToNumber3(self):
        self.assertEqual( symbolToNumber('T'), 3)

class TestNumberToSymbol( unittest.TestCase ):
    def test_NumberToSymbol0(self):
        self.assertEqual( numberToSymbol( 0 ), 'A')
    def test_NumberToSymbol3(self):
        self.assertEqual( numberToSymbol( 3 ), 'T')

class TestPatternToNumber( unittest.TestCase ):
    def test_PatternToNumber0(self):
        self.assertEqual( patternToNumber('AGT'), 11)

class TestNumberToPattern( unittest.TestCase ):
    def test_NumberToPattern0(self):
        self.assertEqual( numberToPattern( 9904, 7), 'GCGGTAA')

class TestFreqWordsBySorting( unittest.TestCase ):
    def test_findFreqWordsBySorting0(self):
        self.assertEqual( findFreqWordsBySorting( 'AAGCAAAGGTGGG', 2), {'AA', 'GG'} )


if __name__ == '__main__':
    unittest.main()
