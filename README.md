#genmasks
Generate JtR compatible masks from dumps and words.


Generate masks from dumps
-------------------------

Convert a password dump to a list of masks.

Example usage:

```
./gen_masks_from_dump.py rockyou.txt | column -t
Matches Mask                    Keyspace
688722  ?l?l?l?l?l?l?l?l        208827064576
601847  ?l?l?l?l?l?l            308915776
585660  ?l?l?l?l?l?l?l          8031810176
517351  ?l?l?l?l?l?l?l?l?l      5429503678976
487431  ?d?d?d?d?d?d?d          10000000
478198  ?d?d?d?d?d?d?d?d?d?d    10000000000
428300  ?d?d?d?d?d?d?d?d        100000000
420390  ?l?l?l?l?l?l?d?d        30891577600
417359  ?l?l?l?l?l?l?l?l?l?l    141167095653376
...
```

Generate masks for words
------------------------

From a word, generate all possible JtR masks with permutations on the word.

Example usage:

```
./gen_masks_from_word.py hello 6
[Hh][Ee3][Ll1|][Ll1|][Oo0]?d
[Hh][Ee3][Ll1|][Ll1|][Oo0]?s
[Hh][Ee3][Ll1|][Ll1|][Oo0]?u
[Hh][Ee3][Ll1|][Ll1|][Oo0]?l
?d[Hh][Ee3][Ll1|][Ll1|][Oo0]
?s[Hh][Ee3][Ll1|][Ll1|][Oo0]
?u[Hh][Ee3][Ll1|][Ll1|][Oo0]
?l[Hh][Ee3][Ll1|][Ll1|][Oo0]
```


Using masks with John the Ripper
--------------------------------

I usually end up doing something like this:

```
for mask in $(cat generated_masks); do john hashes --mask="$mask"; done
```
