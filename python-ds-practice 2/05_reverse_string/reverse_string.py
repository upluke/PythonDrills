# https://www.journaldev.com/23647/python-reverse-string
def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # return phrase[::-1]
    # return ''.join(reversed(phrase))
    if len(phrase) == 1:
        return phrase
    return reverse_string(phrase[1:]) + phrase[0]


print(reverse_string('awesome'))
print(reverse_string('sauce'))
