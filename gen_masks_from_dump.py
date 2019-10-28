#!/usr/bin/env python3
import sys


def mask_from_password(password):
    mask=""
    for char in password:
        if char.isdigit():
            mask += "?d"
        elif char.islower():
            mask += "?l"
        elif char.isupper():
            mask += "?u"
        else:
            mask += "?s"
    return mask


def keyspace_of_mask(mask):
    keyspace = 1
    for charset in mask:
        if charset == 'd':
            keyspace *= 10
        elif charset == 'l':
            keyspace *= 26
        elif charset == 'u':
            keyspace *= 26
        elif charset == 's':
            keyspace *= 33

    return keyspace


if len(sys.argv) != 2:
    print("Usage : " + sys.argv[0] + " <path to dump file>")
    exit(-1)

with open(sys.argv[1], errors='ignore') as password_file:
    passwords = password_file.read().splitlines()

masks = {}
for password in passwords:

    mask = mask_from_password(password)

    if mask in masks:
        masks[mask] += 1
    else:
        masks[mask] = 1

smasks = sorted(masks, key=masks.get, reverse=True)

print("Matches\tMask\t\tKeyspace")
for mask in smasks:
    print("{}\t{}\t\t{}".format(str(masks[mask]), mask, keyspace_of_mask(mask)))
