from modlist import modlist, insertion, relocation

master_list = [1, 2, 3]


def test_prepend():
    assert modlist(master_list, prepend=[0]) == [0, 1, 2, 3]


def test_append():
    assert modlist(master_list, append=[4]) == [1, 2, 3, 4]


def test_insert():
    assert modlist(master_list, insert=[
        insertion(2.5, after=2),
        insertion(1.5, before=2)
    ]) == [1, 1.5, 2, 2.5, 3]


def test_remove():
    assert modlist(master_list, remove=[2]) == [1, 3]


def test_move():
    assert modlist(master_list, move=[
        relocation(2, after=3),
        relocation(3, before=1)
    ]) == [3, 1, 2]


def test_tuple():
    assert modlist(tuple(master_list), move=[
        relocation(3, before=1)
    ]) == (3, 1, 2)
