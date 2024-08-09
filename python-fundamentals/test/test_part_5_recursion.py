from src.part_5_recursion import flatten,deep_entries
import pytest

@pytest.mark.it("for flatten func input is basic list")
def test_flatten_func_01():
    test_input_list = [1, 2, 3]
    assert flatten(test_input_list) == [1, 2, 3]


@pytest.mark.it("for flatten func input is single level nested list")
def test_flatten_func_02():
    test_input_list = [1, 2, [3, 4]]
    assert flatten(test_input_list) == [1, 2, 3, 4]


@pytest.mark.it("for flatten func input is multi level nested list with default depth")
def test_flatten_func_03():
    test_input_list = [1, 2, [3, [4, [5, 6]]]]
    assert flatten(test_input_list) == [1, 2, 3, [4, [5, 6]]]


@pytest.mark.it("for flatten func input is multi level nested list with depth =2")
def test_flatten_func_04():
    test_input_list = [1, 2, [3, [4, [5, 6]]]]
    depth = 2
    assert flatten(test_input_list, depth) == [1, 2, 3, 4, [5, 6]]


@pytest.mark.it("for flatten func input is multi level nested list with depth =3")
def test_flatten_func_05():
    test_input_list = [1, 2, [3, [4, [5, 6]]]]
    depth = 3
    assert flatten(test_input_list, depth) == [1, 2, 3, 4, 5, 6]


@pytest.mark.it("for flatten func input is multi level nested list with depth =25")
def test_flatten_func_05():
    test_input_list = [1, 2, [3, [4, [5, 6]]]]
    depth = 25
    assert flatten(test_input_list, depth) == [1, 2, 3, 4, 5, 6]


@pytest.mark.it("for deep_entries func input is basic dict")
def test_deep_entries_func_01():
    test_input_dict = {'name': 'Sam'}
    assert deep_entries(test_input_dict) == (('name', 'Sam'),)


@pytest.mark.it("for deep_entries func input is dict with 2 entries")
def test_deep_entries_func_02():
    test_input_dict = { 'name': 'Sam', 'fave_book': '50 Shades of JavaScript' }
    assert deep_entries(test_input_dict) == (('name', 'Sam'), ('fave_book', '50 Shades of JavaScript'))


@pytest.mark.it("for deep_entries func input is single level nested dict")
def test_deep_entries_func_05():
    test_input_dict = { 'name': 'Sam', 'pets': {'name': 'fido'}}
    assert deep_entries(test_input_dict) == (('name', 'Sam'),('pets',(('name', 'fido'),)))


@pytest.mark.it("for deep_entries func input is multi level nested dict")
def test_deep_entries_func_05():
    test_input_dict = {
        'name': 'Sam',
        'pets': {'name': 'Fido'},
        'fave_book': { 'title': '50 Shades of JavaScript', 'author': { 'first_name': 'Cody', 'last_name': 'Smutt' }}
    }
    assert deep_entries(test_input_dict) == (
        ('name', 'Sam'),
        ('pets', (('name', 'Fido'),)),
        ('fave_book', (('title', '50 Shades of JavaScript'), ('author', (('first_name', 'Cody'), ('last_name', 'Smutt')))))
    )


