def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # if ord(to_swap)<97:
    #     phrase.replace(to_swap,'_')
    # else:
    phrase = phrase.replace(to_swap, '_')
    if to_swap.islower():  # ord(to_swap) >= 97
        phrase = phrase.replace(to_swap.upper(), to_swap)
        phrase = phrase.replace('_', to_swap.upper())
    else:
        phrase = phrase.replace(to_swap.lower(), to_swap)
        phrase = phrase.replace('_', to_swap.lower())
    return phrase


print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))
