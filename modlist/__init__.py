"""Library for declarative list manipulation."""


def modlist(lst, **kwargs):
    """Perform a series of operations on a list."""
    output = lst[:]

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

    return output


class insertion(object):
    """Class representing insertion into a list."""

    def __init__(self, value, after=None, before=None):
        """Define an insertion after and/or before a given value."""
        self.value = value
        self.after = after
        self.before = before
