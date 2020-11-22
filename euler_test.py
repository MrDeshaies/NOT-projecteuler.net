import unittest
from euler import *


class TestEuler(unittest.TestCase):

    def test_fact1(self):
        self.assertEqual(fact(1), [1])
    
    def test_fact2(self):
        self.assertEqual(fact(2), [1,2])
    
    def test_fact3(self):
        self.assertEqual(fact(3), [1,3])

    def test_fact4(self):
        self.assertEqual(fact(4), [1,2,4])
    
    def test_fact26(self):
        self.assertEqual(fact(26), [1,2,13,26])

    def test_fact5(self):
        self.assertEqual(fact(5), [1,5])

    def test_fact8(self):
        self.assertEqual(fact(8), [1,2,4,8])
    
    def test_fact24(self):
         self.assertEqual(fact(24), [1,2,3,4,6,8,12,24])
    
    def test_fact41(self): #large-ish prime
         self.assertEqual(fact(41), [1,41])
    
    def test_factLessItself(self):
        # 1 is a special case ?
        self.assertTrue(len(factLessItself(1)) == 0, "1 should yield no factors")
        for x in range(2,100):
            expectedFactors = fact(x)
            expectedFactors.pop() # get rid of itself
            self.assertEqual(factLessItself(x), expectedFactors)
    
    def test_isPrime_negative(self):
        self.assertFalse(isPrime(-1))
    
    def test_primality(self):
        UPPER_LIMIT = 101
        sieve = find_primality(UPPER_LIMIT)
        self.assertEqual(len(sieve), UPPER_LIMIT+1)
        for i in range(2,UPPER_LIMIT+1):
            self.assertEqual(sieve[i], isPrime(i), "sieve failed for value " + str(i))
    
    def test_list_primes(self):
        self.assertEqual(list_primes(10), [2,3,5,7])
        self.assertEqual(list_primes(11), [2,3,5,7,11])
    
    def test_pandigital_partial(self):
        self.assertTrue(pandigital_partial(1))
        self.assertTrue(pandigital_partial(12))
        self.assertTrue(pandigital_partial(123))
        self.assertTrue(pandigital_partial(123456789))
        self.assertTrue(pandigital_partial(918273645))

        self.assertFalse(pandigital_partial(2))
        self.assertFalse(pandigital_partial(11))
        self.assertFalse(pandigital_partial(13))
        self.assertFalse(pandigital_partial(1235))
        self.assertFalse(pandigital_partial(12350))
        self.assertFalse(pandigital_partial(1234567891))
    
    def test_pandigital(self):
        self.assertFalse(pandigital(1))
        self.assertFalse(pandigital(12))
        self.assertFalse(pandigital(123))
        self.assertFalse(pandigital(1234567891))
        self.assertFalse(pandigital("1234567891"))

        self.assertTrue(pandigital(123456789))
        self.assertTrue(pandigital(918273645))
        self.assertTrue(pandigital("123456789"))
    
    def test_sum_digits(self):
        self.assertEqual(1, sum_digits(1))
        self.assertEqual(2, sum_digits(2))
        self.assertEqual(3, sum_digits(12))
        self.assertEqual(10, sum_digits(1234))
        self.assertEqual(36, sum_digits(9999))
    
    def test_convert_convergents_to_fraction(self):
        cctf = convert_convergents_to_fraction
        # single values
        self.assertEqual(Fraction(1), cctf([1]))
        self.assertEqual(Fraction(2), cctf([2]))

        # two values
        self.assertEqual(Fraction(3,2), cctf([1,2]))
        self.assertEqual(Fraction(7,3), cctf([2,3]))

        # three values
        self.assertEqual(Fraction(37,16), cctf([2,3,5]))
    
    def test_is_permutation(self):
        self.assertTrue(is_permutation(1,1))
        self.assertTrue(is_permutation(123,321))
        self.assertTrue(is_permutation(123,213))
        self.assertTrue(is_permutation(112,121))

        self.assertFalse(is_permutation(1,2))
        self.assertFalse(is_permutation(12,34))
        self.assertFalse(is_permutation(1122,1233))


if __name__ == '__main__':
    unittest.main()