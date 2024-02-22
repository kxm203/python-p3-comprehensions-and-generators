#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    if even_numbers:
        return even_numbers
    else:
        return [] 


def make_exclamation(sentence_list):
    if not sentence_list:
        return []
    exclaimed_sentences = [sentence + '!' for sentence in sentence_list]
    return exclaimed_sentences