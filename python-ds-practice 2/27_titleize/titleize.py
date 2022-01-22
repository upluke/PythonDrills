def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    res = ""
    for word in phrase.split(' '):
        res += " " + word.capitalize()
    return res


print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))
