from src.for_each import for_each, do_some_stuff


def test_empty_list():
    lst = ['danika','cat']
    input = []
    expected = lst

    assert for_each(input,do_some_stuff) == expected


def test_do_some_stuff_is_invoked_twice():
    lst = []
    input = ['danika','cat']
    def test_func(arg):
        return lst.append(arg)
    for_each(input,test_func)
    assert lst == input
    
    # assert for_each(input,do_some_stuff) == excepted


def test_single_item_is_invoked():
    pass

def if_do_some_stuff_does_anything():
    pass
