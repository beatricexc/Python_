

def search4vowels(phrase: str) -> set:
    """ Display any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Returns a set of the 'letters' found in'phrase'."""
    return set(letters).intersection(set(phrase))
