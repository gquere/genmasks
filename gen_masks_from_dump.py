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


if len(sys.argv) != 2:
    print("Usage : " + sys.argv[0] + " <path to dump file>")
    exit(-1)

with open(sys.argv[1], errors='ignore') as password_file:
    passwords = password_file.read().splitlines()

masks = {}
for password in passwords:
    if len(password) != 8:
        continue

    mask = mask_from_password(password)

    if mask in masks:
        masks[mask] += 1
    else:
        masks[mask] = 1

for mask in masks:
    print(str(masks[mask]) + " " + mask)
