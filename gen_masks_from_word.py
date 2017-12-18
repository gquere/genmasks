#!/usr/bin/env python3
import sys


# GENERATE MASK FOR WORD #######################################################
def pattern_from_word(word):
    pattern = ""
    for letter in word:
        if letter == 'a':
            pattern += '[Aa4@]'
        if letter == 'b':
            pattern += '[Bb]'
        if letter == 'c':
            pattern += '[Cc(]'
        if letter == 'd':
            pattern += '[Dd]'
        if letter == 'e':
            pattern += '[Ee3]'
        if letter == 'f':
            pattern += '[Ff]'
        if letter == 'g':
            pattern += '[Gg6]'
        if letter == 'h':
            pattern += '[Hh]'
        if letter == 'i':
            pattern += '[Ii1|]'
        if letter == 'j':
            pattern += '[Jj]'
        if letter == 'k':
            pattern += '[Kk]'
        if letter == 'l':
            pattern += '[Ll1|]'
        if letter == 'm':
            pattern += '[Mm]'
        if letter == 'n':
            pattern += '[Nn]'
        if letter == 'o':
            pattern += '[Oo0]'
        if letter == 'p':
            pattern += '[Pp]'
        if letter == 'q':
            pattern += '[Qq]'
        if letter == 'r':
            pattern += '[Rr]'
        if letter == 's':
            pattern += '[Ss5$]'
        if letter == 't':
            pattern += '[Tt7]'
        if letter == 'u':
            pattern += '[Uu]'
        if letter == 'v':
            pattern += '[Vv]'
        if letter == 'w':
            pattern += '[Ww]'
        if letter == 'x':
            pattern += '[Xx+]'
        if letter == 'y':
            pattern += '[Yy]'
        if letter == 'z':
            pattern += '[Zz2]'

    return pattern


# GENERATE PADDING LIST ########################################################
def base_convert(i, b):
    result = []
    while i > 0:
            result.insert(0, i % b)
            i = i // b

    return result

# generate all combinations of the length needed in base 4 which will later
# be translated to mask values (?d, ?s, ?u and ?l)
def generate_padding(padding_length):
    padding = []
    i = 0
    while 1:
        nb = base_convert(i, 4)
        if len(nb) > padding_length:
            break
        while len(nb) < padding_length:
            nb.insert(0, 0)
        padding.append(nb)
        i += 1

    return padding


# GENERATE MASK FROM WORD MASK AND PADDING #####################################
def convert_and_print_mask(mask):
    mask_string = ""

    for elem in mask:
        if elem == 0:
            mask_string += '?d'
        elif elem == 1:
            mask_string += '?s'
        elif elem == 2:
            mask_string += '?u'
        elif elem == 3:
            mask_string += '?l'
        else:
            mask_string += elem

    print(mask_string)


def generate_masks(pattern, paddings):
    padding_length = len(paddings)
    paddings_op = list(paddings)

    for pattern_index in range(len(paddings[0]) + 1):
        for padding in paddings_op:
            a = list(padding)
            a.insert(pattern_index, pattern)
            convert_and_print_mask(a)
        paddings_op = list(paddings)


# MAIN #########################################################################
if len(sys.argv) != 3:
    print("usage : " + sys.argv[0] + " <word> <passwd_len>")
    exit(-1)


word_len = len(sys.argv[1])
mask_len = int(sys.argv[2])
padding_length = mask_len - word_len

pattern = pattern_from_word(sys.argv[1])
padding = generate_padding(padding_length)

generate_masks(pattern, padding)
