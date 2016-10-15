#-*- coding: utf-8 -*-
from Crypto.Util.strxor import strxor_c

import re

def cg03_single_byte_xor_cipher(value):
    result = get_more_scored_text(value)

    return result

def get_more_scored_text(value):
    maximum_score = 0
    text_with_maximum_score = '';

    text_decoded = value.decode('hex')
    for code in range(0, 256):
        text_decoded = fixed_xor(text_decoded, code)
        score = get_text_score(text_decoded)
        if score > maximum_score:
            maximum_score = score
            text_with_maximum_score = text_decoded

    return text_with_maximum_score


def fixed_xor(value1, char):
    result = strxor_c(value1, char)

    return result

def get_text_score(text_decoded):
    score = 0

    for char in text_decoded:
        if char == 'e':
            score += 5
        elif char == 't':
            score += 4
        elif char == 'a':
            score += 4
        elif char == 'o':
            score += 3
        elif char == 'i':
            score += 3
        elif char == 'n':
            score += 2
        elif char == ' ':
            score += 2
        elif char == 's':
            score += 2
        elif char == 'h':
            score += 2

    return score
