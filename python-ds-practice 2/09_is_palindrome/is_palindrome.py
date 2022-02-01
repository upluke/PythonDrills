def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # solution:
    # normalized = phrase.lower().replace(' ', '')
    # return normalized == normalized[::-1]

    clean_input = get_clean_input(phrase)
    return clean_input == clean_input[::-1]


def get_clean_input(input):
    new_input = ""
    for char in input:
        if char.isalpha():
            new_input += char.lower()
    return new_input


print(is_palindrome('tacocat'))
print(is_palindrome('robert'))
print(is_palindrome('Noon'))
print(is_palindrome('taco cat'))
