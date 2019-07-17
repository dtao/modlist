"""Library for declarative list manipulation."""


def modlist(lst, **kwargs):
    """Perform a series of operations on a list."""
    output = list(lst)

    if 'prepend' in kwargs:
        output = kwargs['prepend'] + output

    if 'append' in kwargs:
        output = output + kwargs['append']

    for insertion in kwargs.get('insert', []):
        if insertion.after:
            after_index = output.index(insertion.after)
            output.insert(after_index + 1, insertion.value)
        elif insertion.before:
            before_index = output.index(insertion.before)
            output.insert(before_index, insertion.value)

    for removal in kwargs.get('remove', []):
        index = output.index(removal)
        output.pop(index)

    for relocation in kwargs.get('move', []):
        index = output.index(relocation.value)
        output.pop(index)
        if relocation.after:
            after_index = output.index(relocation.after)
            output.insert(after_index + 1, relocation.value)
        elif relocation.before:
            before_index = output.index(relocation.before)
            output.insert(before_index, relocation.value)

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
