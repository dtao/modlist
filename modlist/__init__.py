"""Library for declarative list manipulation."""


def modlist(lst, **kwargs):
    """Perform a series of operations on a list."""
    output = list(lst)

    if 'prepend' in kwargs:
        output = kwargs['prepend'] + output

    if 'append' in kwargs:
        output = output + kwargs['append']

    def remove(value):
        index = output.index(value)
        output.pop(index)

    def insert(value, location):
        if location.after:
            after_index = output.index(location.after)
            output.insert(after_index + 1, value)
        elif location.before:
            before_index = output.index(location.before)
            output.insert(before_index, value)

    for insertion in kwargs.get('insert', []):
        insert(insertion.value, insertion)

    for removal in kwargs.get('remove', []):
        remove(removal)

    for relocation in kwargs.get('move', []):
        remove(relocation.value)
        insert(relocation.value, relocation)

    if isinstance(lst, tuple):
        output = tuple(output)

    return output


class insertion(object):
    """Class representing insertion into a list."""

    def __init__(self, value, after=None, before=None):
        """Define an insertion after and/or before a given value."""
        self.value = value
        self.after = after
        self.before = before


class relocation(object):
    """Class representing relocation of an item in a list."""

    def __init__(self, value, after=None, before=None):
        """Define a relocation of a given value relative to another value."""
        self.value = value
        self.after = after
        self.before = before
