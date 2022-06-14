# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:17:39 2020

@author: Albert Tran
"""

# %% -------------------------------------------------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------------------------------------------------
import glob
import numpy as np
import string
import unicodedata
import pkg_resources

# %% -------------------------------------------------------------------------------------------------------------------
# Data Path
#-----------------------------------------------------------------------------------------------------------------------
DATA_PATH = pkg_resources.resource_filename(__name__, 'data/')

# %% -------------------------------------------------------------------------------------------------------------------
# File Processing
#-----------------------------------------------------------------------------------------------------------------------
all_letters = string.ascii_letters + " .,;'"
n_letters   = len(all_letters)

# Turn a Unicode string to plain ASCII, thanks to https://stackoverflow.com/a/518232/2809427
def unicode_to_ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )

def read_lines(filename):
    '''
    Reads in a file and returns a list of lines all coverted to unicode.
    '''
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        return [unicode_to_ascii(line.strip()) for line in lines]

def get_data():
    category_lines = {}
    categories     = []
    for filename in glob.glob(DATA_PATH + r'*.txt'):
        category = filename[filename.rfind('\\')+1: filename.rfind('.')]
        categories.append(category)
        category_lines[category] = read_lines(filename)

    return category_lines

def letter_to_index(letter):
    '''
    Find a letter from all_letters. For example, 'a'=0
    '''
    return all_letters.find(letter)


def letter_to_vector(letter):
    '''
    Returns a one-hot encoded vector for the letter.
    '''
    x = np.zeros((1, n_letters))
    x[0, letter_to_index(letter)] = 1
    return x
    
def word_to_tensor(word, min_len=0):
    '''
    Returns a numpy tensor representing each letter in the word.
    Dimension of the returned tensor is (min_word_len, 1, n_letters).
    Here, min_word_len is max(word_len, min_len).
    '''
    word_vectors = []
    for letter in word:
        word_vectors.append(letter_to_vector(letter))
    
    # Add padding to word vectors
    if len(word_vectors) < min_len:
        num_pad = min_len - len(word_vectors)
        for i in range(num_pad):
            word_vectors.append(np.zeros((1, n_letters)))
    
    return np.c_[word_vectors]
    


