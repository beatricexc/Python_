def search4vowels(phrase:str)-> set:
    """Display any vowels found in an asked-for word. """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str = 'aeiou') -> set:
    """Return a set of the 'letters' argument found in 'phrase'."""
    return set(letters).intersection(set(phrase))
