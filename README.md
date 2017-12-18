#genmasks
Generate JtR compatible masks from dumps and words.


Generate masks from dumps
-------------------------

Convert a password dump to a list of masks.

Example usage:

    ```
    ./gen_masks_from_dump.py rockyou.txt | sort -n
    ...
    31381 ?u?u?u?u?u?u?d?d
    37622 ?l?l?l?d?d?d?d?d
    39505 ?u?u?u?u?u?u?u?u
    48545 ?l?l?d?d?d?d?d?d
    152427 ?l?l?l?l?l?d?d?d
    189881 ?l?l?l?l?l?l?l?d
    235393 ?l?l?l?l?d?d?d?d
    420390 ?l?l?l?l?l?l?d?d
    428300 ?d?d?d?d?d?d?d?d
    688722 ?l?l?l?l?l?l?l?l
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
