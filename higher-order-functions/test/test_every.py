from src.every import every,is_even

def test_if_inner_func_is_evoke():
    is_function_evoke = False

    def test_func(arg):
        nonlocal is_function_evoke 
        is_function_evoke = True


    expected = every([1,2],test_func)
    assert expected == every([1,2],is_even)


