from src.part_1_human_resources import make_name_tags, create_poll
import pytest
from data.poll_data import nc_fruit_bowl

@pytest.mark.it("Test with empty guest list")
def test_empty_list():
    guests_list = []
    assert make_name_tags(guests_list) == []


@pytest.mark.it("Test with guest list input")
def test_guest_list():
    guest_list = [
  {
    'title': 'Mr',
    'forename': 'Sam',
    'surname': 'Caine',
    'age': 30,
    'company': 'Northcoders',
  },
  {
    'title': 'Mr',
    'forename': 'Kermit',
    'surname': 'The Frog',
    'age': 35,
    'company': 'Jim Henson Studios',
  },
]
    assert make_name_tags(guest_list) == [
  {
    'title': 'Mr',
    'forename': 'Sam',
    'surname': 'Caine',
    'age': 30,
    'company': 'Northcoders',
    'name_tag': 'Mr Sam Caine, Northcoders',
  },
  {
    'title': 'Mr',
    'forename': 'Kermit',
    'surname': 'The Frog',
    'age': 35,
    'company': 'Jim Henson Studios',
    'name_tag': 'Mr Kermit The Frog, Jim Henson Studios'
  }
]


@pytest.mark.it("test with guest list no side effect")
def test_no_side_effect():
    guests_list = [
  {
    'title': 'Mr',
    'forename': 'Sam',
    'surname': 'Caine',
    'age': 30,
    'company': 'Northcoders',
  },
  {
    'title': 'Mr',
    'forename': 'Kermit',
    'surname': 'The Frog',
    'age': 35,
    'company': 'Jim Henson Studios',
  },
]
    copy_guests_list = [guest.copy() for guest in  guests_list]
    make_name_tags(guests_list)
    assert make_name_tags(guests_list) == make_name_tags(copy_guests_list)

@pytest.mark.it("Test create a pool for empty list returns empty list")
def test_create_pool_for_empty_list():
    test_list = []
    assert create_poll(test_list) == []

@pytest.mark.it("Test create a pool with dublicate items returns calculate and write amount of item")
def test_create_pool_with_dublicates():
    assert create_poll(["cake", "biscuit", "biscuit"]) == {'cake' : 1, 'biscuit' : 2}

@pytest.mark.it("Test create a pool with same items returns calculate and write amount of item")
def test_create_pool_with_same_items():
    assert create_poll(["dog", "dog", "dog"]) == {'dog' : 3}

@pytest.mark.it("Test create a pool using data file returns calculate and write amount of item")
def test_create_pool_from_data_file():
    assert create_poll(nc_fruit_bowl) == {'apple': 276,'pear': 223,'banana': 263,'orange': 238,'lonesome plum': 1}