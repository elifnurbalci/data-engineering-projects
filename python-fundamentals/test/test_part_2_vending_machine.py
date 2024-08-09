import pytest
from src.part_2_vending_machine import VendingMachine

@pytest.fixture(scope='function')
def machine():
    return VendingMachine()

@pytest.mark.describe('All Vending Machine Methods')
class TestVendingMachine:

    @pytest.mark.it('has valid credit attribute')
    def test_credit(self, machine):
        assert machine.credit == 0

    @pytest.mark.it('has expected stock attributes')
    def test_stock(self, machine):
        assert machine.stock['A'] == {}
        assert machine.stock['B'] == {}
        assert machine.stock['C'] == {}

    @pytest.mark.it('adds credit to initial amount')
    def test_add_credit(self, machine):
        machine.add_credit(75)
        assert machine.credit == 75
        new_machine = VendingMachine()
        new_machine.add_credit(62)
        assert new_machine.credit == 62

    @pytest.mark.it('accumulates credit')
    def test_accumulate_credit(self, machine):
        machine.add_credit(19)
        assert machine.credit == 19
        machine.add_credit(33)
        assert machine.credit == 52

    @pytest.mark.it('validates when there is sufficient credit for an item')
    def test_sufficient_credit(self, machine):
        machine.add_credit(36)
        assert machine.credit_checker(30)

    @pytest.mark.it('validates when there is insufficient credit for an item')
    def test_insufficient_credit(self, machine):
        machine.add_credit(36)
        assert not machine.credit_checker(44)
    
    @pytest.mark.it('adds item to stock')
    def test_add_stock(self,machine):
        item = { 'name': "mars_bar", 'price': 50, 'quantity': 6 }
        row = 'A'
        assert machine.add_stock(item, row) == {'A': {'name': 'mars_bar', 'price': 50, 'quantity': 6},'B': {},'C': {}}
    
    @pytest.mark.it('if item is in stok return an error message')
    def test_add_dublicate_item(self, machine):
        machine.stock = {'A': {'name': 'mars_bar', 'price': 50, 'quantity': 6},'B': {},'C': {}}
        item = { 'name': "mars_bar", 'price': 50, 'quantity': 6 }
        row = 'A'
        assert machine.add_stock(item,row) == "This item already exists, please add another one!"
    
    @pytest.mark.it('purchase item if credit less than item price returns error message')
    def test_purchase_not_completed(self, machine):
        item = { 'name': "mars_bar", 'price': 50, 'quantity': 6 }
        row = 'A'
        machine.add_stock(item, row)
        machine.add_credit(30)
        assert machine.purchase_item(row) == "Insufficient credit!"

    @pytest.mark.it('purchase item if credit less than item price returns error message and remain stock and credit info')
    def test_purchase_not_completed_return_credit_and_stock_info(self, machine):
        item = { 'name': "mars_bar", 'price': 50, 'quantity': 6 }
        row = 'A'
        machine.add_stock(item, row)
        machine.add_credit(30)
        assert machine.stock[row]['quantity'] == 6
        assert machine.credit == 30

    @pytest.mark.it('price less than credit return item and adjust credit according to item price')
    def test_purchase_item(self, machine):
        item = { 'name': "mars_bar", 'price': 50, 'quantity': 6 }
        row = 'A'
        machine.add_stock(item, row)
        machine.add_credit(60)
        assert machine.purchase_item(row)  == "mars_bar"
        assert machine.stock[row]['quantity'] == 5
        assert machine.credit == 10