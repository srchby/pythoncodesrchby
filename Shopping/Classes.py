class User:
  def __init__(self, name, money, cart):
    self.name = name
    self.money = money
    self.cart = cart

class Item:
  def __init__(self, id, name_obj, price):
    self.id = id
    self.name_obj = name_obj
    self.price = price