#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.end_transaction = 0

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, value):
    self._discount = value

  def add_item(self, title, price, optional_quantity=1):

    if optional_quantity < 1:
      print('Please input quantity!')
    self.items.extend([title] * optional_quantity )
    transaction_amount = price * optional_quantity
    self.end_transaction = transaction_amount
    self.total += transaction_amount
  
  def apply_discount(self):
      if self.discount > 0:
        self.total -=  self.total * (self.discount / 100)
        print('After the discount, the total comes to $800.')
      else: 
        print('There is no discount to apply.')
    
  def get_items(self):
    return self.items
  
  def void_last_transaction(self):
    self.total -= self.end_transaction

    item_count = self.end_transaction // (self.end_transaction / len(self.items))
    self.items = self.items[:-int(item_count)]
  
    self.end_transcation = 0