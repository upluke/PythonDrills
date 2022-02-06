def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # solution:
    # there's a built-in method for this!
    # return phrase.title()
    # or, if you didn't know that, could capitalize each word by hand
    # return ' '.join([s.capitalize() for s in phrase.split(' ')])

    res = ""
    for word in phrase.split(' '):
        res += " " + word.capitalize()
    return res


print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))
