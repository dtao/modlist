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
        if location.get('after'):
            after_index = output.index(location['after'])
            output.insert(after_index + 1, value)
        elif location.get('before'):
            before_index = output.index(location['before'])
            output.insert(before_index, value)

    for value, location in kwargs.get('insert', []):
        insert(value, location)

    for removal in kwargs.get('remove', []):
        remove(removal)

    for value, location in kwargs.get('move', []):
        remove(value)
        insert(value, location)

    if isinstance(lst, tuple):
        output = tuple(output)

    return output
