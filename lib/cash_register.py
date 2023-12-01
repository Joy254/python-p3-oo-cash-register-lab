#!/usr/bin/env python3

class CashRegister:
  pass
  def __init__(self, discount_percentage=0):
        self.items = []
        self.last_transaction = 0
        self.total = 0
        
  def apply_discount(self):
        if hasattr(self, 'discount_percentage') and self.discount_percentage > 0:
            discount_factor = 1 - (self.discount_percentage / 100)
            self.total *= discount_factor
        else:
            print("There is no discount to apply.")

  def test_discount_attribute(self):
    (self.cash_register.discount_percentage == 0)
    (self.cash_register_with_discount.discount_percentage == 20)
  
  def test_apply_discount_success_message(self):
    
    captured_out = io.StringIO()
    sys.stdout = captured_out
    self.cash_register_with_discount.add_item("macbook air", 1000)
    self.cash_register_with_discount.apply_discount()
    sys.stdout = sys.__stdout__
    (captured_out.getvalue() == "There is no discount to apply.\n")

  def test_apply_discount_reduces_total(self):
    self.cash_register_with_discount.add_item("macbook air", 1000)
    self.cash_register_with_discount.apply_discount()
    (self.cash_register_with_discount.total == 1000 * 0.8)

  def add_item(self, item_name,price_per_item ,quantity=1):
        item_total = quantity * price_per_item
        self.items.extend([item_name] * quantity)
        self.last_transaction = item_total
        self.total += item_total

  def test_add_item(self):
    self.cash_register.add_item("eggs", 0.98)
    assert(self.cash_register.total == 0.98)
    self.reset_register_totals()
  def void_last_transaction(self):
        if self.last_transaction > 0:
            self.total -= self.last_transaction
            self.items.pop()
            self.last_transaction = 0
        else:
            print("No transaction to void.")

  def test_items_list_without_multiples(self):
    '''returns an array containing all items that have been added'''
    new_register = CashRegister()
    new_register.add_item("eggs", 1.99)
    new_register.add_item("tomato", 1.76)
    assert(new_register.items == ["eggs", "tomato"])

def test_items_list_with_multiples(self):
    '''returns an array containing all items that have been added, including multiples'''
    new_register = CashRegister()
    new_register.add_item("eggs", 1.99, 2)
    new_register.add_item("tomato", 1.76, 3)
    assert(new_register.items == ["eggs", "eggs", "tomato", "tomato", "tomato"])


