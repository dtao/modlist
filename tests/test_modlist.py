from modlist import modlist, insertion

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
