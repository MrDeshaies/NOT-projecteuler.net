import unittest
from euler_054 import *

class Test54(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_parse_hand(self):
        cards = parse_hand("8C KC 7S TC 2D")
        print(cards)
        self.assertEqual(len(cards), 5)
        # values re-arranged by sort
        self.assertEqual(cards[0].value, "2")
        self.assertEqual(cards[0].suit,  "D")
        self.assertEqual(cards[1].value, "7")
        self.assertEqual(cards[1].suit,  "S")
        self.assertEqual(cards[4].value, "K")
        self.assertEqual(cards[4].suit,  "C")
    
    def test_numerical_value(self):
        c3 = Card._make(['3','H'])
        c13 = Card._make(['K', 'H'])
        self.assertEqual(3,   c3.numerical_value())
        self.assertEqual(13, c13.numerical_value())
    
    def test_card_values_not_x(self):
        self.assertEqual([2,4], card_values_not_x(parse_hand("2H 3Q 3S 3H 4D"),3))
        self.assertEqual([3,3,3,4], card_values_not_x(parse_hand("2H 3Q 3S 3H 4D"),2))

    
    def test_royal_flush(self):
        # royal in 2 different suits
        self.assertEqual(10, royal_flush(parse_hand("TH JH QH KH AH")))
        self.assertEqual(10, royal_flush(parse_hand("TS JS QS KS AS")))

        # mismatch of suit
        self.assertEqual(0, royal_flush(parse_hand("TH JS QH KH AH")))

        # starting at 9
        self.assertEqual(0, royal_flush(parse_hand("9H TH JH QH KH")))
    
    def test_straight_flush(self):
        # in 2 different suits
        self.assertEqual(10, straight_flush(parse_hand("TH JH QH KH AH")))
        self.assertEqual(10, straight_flush(parse_hand("TS JS QS KS AS")))

        # starting at 2
        self.assertEqual(2, straight_flush(parse_hand("2S 3S 4S 5S 6S")))
        # starting at 3
        self.assertEqual(3, straight_flush(parse_hand("3S 4S 5S 6S 7S")))
        # starting at 9
        self.assertEqual(9, straight_flush(parse_hand("9S TS JS QS KS")))

        # mismatch of suit
        self.assertEqual(0, straight_flush(parse_hand("TH JS QH KH AH")))
        self.assertEqual(0, straight_flush(parse_hand("3S 4H 5S 6S 7S")))
    
    def test_straight(self):
        self.assertEqual(10, straight(parse_hand("TH JD QS KH AH")))
        self.assertEqual(2,  straight(parse_hand("2S 3H 4D 5C 6S")))

        # not consecutive
        self.assertEqual(0, straight_flush(parse_hand("3S 5H 6C 7D 8S")))
    
    def test_flush(self):
        # in 2 different suits
        self.assertEqual(14, flush(parse_hand("TH JH QH KH AH")))
        self.assertEqual(14, flush(parse_hand("TS JS QS KS AS")))
        # random numbers
        self.assertEqual(10, flush(parse_hand("2S 5S 6S 7S TS")))

        # one off
        self.assertEqual(0, flush(parse_hand("TS JH QS KS AS")))
        self.assertEqual(0, flush(parse_hand("2S 5S 6S 7D TS")))
    
    def test_four_of_a_kind(self):
        # with 2s, starting position
        self.assertEqual(2, four_of_a_kind(parse_hand("2H 2Q 2S 6H 2D")))
        # last 4 cards
        self.assertEqual(3, four_of_a_kind(parse_hand("2H 3Q 3S 3H 3D")))

        # 3 is not enough...
        self.assertEqual(0, four_of_a_kind(parse_hand("2H 2Q 2S 6H 6D")))
    
    def test_three_of_a_kind(self):
        # with 2s, starting position
        self.assertEqual(2, three_of_a_kind(parse_hand("2H 5Q 2S 6H 2D")))
        # last 3 cards
        self.assertEqual(3, three_of_a_kind(parse_hand("2H 6Q 3S 3H 3D")))

        # 2 is not enough...
        self.assertEqual(0, three_of_a_kind(parse_hand("2H 2Q 3S 6H 6D")))
    
    def test_two_pairs(self):
        self.assertEqual(5, two_pairs(parse_hand("2H 5Q 2S 6H 5D")))
        self.assertEqual(5, two_pairs(parse_hand("5H 5Q 2S 6H 2D")))
        self.assertEqual(0, two_pairs(parse_hand("5H 5Q 3S 6H 2D")))
    
    def test_pair(self):
        self.assertEqual(5, pair(parse_hand("2H 5Q 3S 6H 5D")))
        self.assertEqual(0, pair(parse_hand("5H 4Q 3S 6H 2D")))
    
    def test_full_house(self):
        # Full House: Three of a kind and a pair.
        self.assertEqual(3, full_house(parse_hand("2H 2Q 3S 3H 3D")))
        # no pair available
        self.assertEqual(0, full_house(parse_hand("2H 3Q 3S 3H 3D")))
    
    def test_high_card(self):
        self.assertEqual(3, high_card(parse_hand("2H 2Q 3S 3H 3D")))
        self.assertEqual(14, high_card(parse_hand("TH JH QH KH AH")))
        self.assertEqual(10, high_card(parse_hand("TH 9H 8H 7H 6H")))
    
    def test_score_hand(self):
        h = parse_hand
        # test royal flush, 1000 + lowest card
        self.assertEqual(1010, score_hand(h("TH JH QH KH AH")))
        # test four of a kind, 800 + kind
        self.assertEqual(802, score_hand(h("2H 2Q 2S 6H 2D")))
        # test two pairs, 300 + highest pair card
        self.assertEqual(305, score_hand(h("5H 5Q 2S 6H 2D")))
        # full house with three-4s
        self.assertEqual(704, score_hand(h("2H 2D 4C 4D 4S")))

    
    def test_find_winner(self):
        h = parse_hand
        self.assertEqual(2, find_winner(h("5H 5C 6S 7S KD"), h("2C 3S 8S 8D TD")))
        self.assertEqual(1, find_winner(h("5D 8C 9S JS AC"), h("2C 5C 7D 8S QH")))
        self.assertEqual(2, find_winner(h("2D 9C AS AH AC"), h("3D 6D 7D TD QD")))
        self.assertEqual(1, find_winner(h("4D 6S 9H QH QC"), h("3D 6D 7H QD QS")))
        self.assertEqual(1, find_winner(h("2H 2D 4C 4D 4S"), h("3C 3D 3S 9S 9D")))
    
    def test_sort_hand(self):
        cards = [Card._make(['A','H']), Card._make(['8','S']), Card._make(['2','H']), Card._make(['K','H'])]
        sort_hand(cards)
        self.assertEqual([c.value for c in cards], ['2','8','K','A'])


if __name__ == '__main__':
    unittest.main()