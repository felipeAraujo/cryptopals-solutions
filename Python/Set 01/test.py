import unittest

import challenge01
import challenge02
import challenge03

class Set1_Challenges_Test_Cases(unittest.TestCase):
    """
    Tests of the Set 1 of challenges of the site cryptopals.com
    """
    
    def test_cg01_hex_to_base64(self):
        self.assertEqual(
            challenge01.cg01_hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'),
            'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        )

    def test_cg02_fixed_xor(self):
        self.assertEqual(
            challenge02.cg02_fixed_xor(
                '1c0111001f010100061a024b53535009181c',
                '686974207468652062756c6c277320657965'
            ),
            '746865206b696420646f6e277420706c6179'
        )

    def test_cg03_singlebyte_xor_cipher(self):
        self.assertEqual(
            challenge03.cg03_single_byte_xor_cipher('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'),
            "Cooking MC's like a pound of bacon"
        )

if __name__ == '__main__':
    unittest.main()

