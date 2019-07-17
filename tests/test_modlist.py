from modlist import modlist

master_list = [1, 2, 3]


def test_prepend():
    assert modlist(master_list, prepend=[0]) == [0, 1, 2, 3]


def test_append():
    assert modlist(master_list, append=[4]) == [1, 2, 3, 4]


def test_insert():
    assert modlist(master_list, insert=[
        (2.5, {'after': 2}),
        (1.5, {'before': 2})
    ]) == [1, 1.5, 2, 2.5, 3]


def test_remove():
    assert modlist(master_list, remove=[2]) == [1, 3]


def test_move():
    assert modlist(master_list, move=[
        (2, {'after': 3}),
        (3, {'before': 1})
    ]) == [3, 1, 2]


def test_tuple():
    assert modlist(tuple(master_list), move=[
        (3, {'before': 1})
    ]) == (3, 1, 2)
