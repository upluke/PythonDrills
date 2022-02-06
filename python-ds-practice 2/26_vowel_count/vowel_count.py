import collections


# VOWELS = set("aeiou")


def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # solution:
    # phrase = phrase.lower()
    # counter = {}

    # for ltr in phrase:
    #     if ltr in VOWELS:
    #         counter[ltr] = counter.get(ltr, 0) + 1

    # return counter

    hp = {}
    for char in phrase.lower():
        if char in ['a', 'e', 'i', 'o', 'u']:
            hp[char] = hp.get(char, 0)+1
    return hp


print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))
