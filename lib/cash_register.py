#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount= 0):
    self.discount = discount
    self.total = 0
    self.items = []
  def add_item(self,title,price,quantity=1):
    self.items.append((title,price,quantity))
    self.total += price * quantity
  def apply_discount(self):
      if self.discount > 0 :
        self.total -= self.total * (self.discount / 100)
      print(f"After the discount, the total comes to ${self.total}.")
