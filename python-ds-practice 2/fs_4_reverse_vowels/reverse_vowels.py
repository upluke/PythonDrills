def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    l, r = 0, len(s)-1
    s_list = list(s)
    vowels = "aeiouAEIOU"
    while l < r:
        if s_list[l] in vowels and s_list[r] in vowels:
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
        elif s_list[l] not in vowels:
            l += 1
        elif s_list[r] not in vowels:
            r -= 1

    return "".join(s_list)
