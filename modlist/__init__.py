"""
Library for declarative list manipulation.

This library consists of a single method, `modlist`, which accepts a list and
a small number of keywords arguments describing modifications to apply to the
list. These modifications are non-destructive and are performed on a copy of
the list, which is then returned.
"""


def modlist(lst, prepend=None, append=None, insert=None, remove=None,
            move=None):
    """Perform a series of operations on a list.

    :param prepend:
        An optional list of values to prepend to the beginning of the list.

    :param append:
        An optional list of values to append to the end of the list.

    :param insert:
        An optional list of tuples describing insertions to be made into the
        list. Each tuple should have the form (value, location) where location
        is a dict comprising the keys 'before' and/or 'after' and specifying
        values before/after which the given value should be inserted.

    :param remove:
        An optional list of values to remove from the list. Note that if a
        value appears multiple times in the list, it will only be removed once
        per specified removal.

    :param move:
        An optional list of tuples indicating values that should be moved to a
        new location in the list. Each tuple should have the form
        (value, location) where location is a dict comprising the keys 'before'
        and/or 'after' and specifying values before/after which the given value
        should be moved.
    """
    output = list(lst)

    if prepend:
        output = prepend + output

    if append:
        output = output + append

    def remove_item(value):
        index = output.index(value)
        output.pop(index)

    def insert_item(value, location):
        if location.get('after'):
            after_index = output.index(location['after'])
            output.insert(after_index + 1, value)
        elif location.get('before'):
            before_index = output.index(location['before'])
            output.insert(before_index, value)

    if insert:
        for value, location in insert:
            insert_item(value, location)

    if remove:
        for removal in remove:
            remove_item(removal)

    if move:
        for value, location in move:
            remove_item(value)
            insert_item(value, location)

    if isinstance(lst, tuple):
        output = tuple(output)

    return output
