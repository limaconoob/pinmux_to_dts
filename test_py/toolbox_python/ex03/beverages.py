class HotBeverage:
  Price = 0.30
  Name = "hot beverage"
  def description(self):
    return "Just some hot water in a cup."
  def __str__(self):
    return "name : " + self.Name + "\nprice : " + str('%.2f' % self.Price) + "\ndescription : " + self.description()

class Coffee(HotBeverage):
  Price = 0.40
  Name = "coffee"
  def description(self):
    return "A coffee, to stay awake."

class Tea(HotBeverage):
  Price = 0.30
  Name = "tea"
  def description(self):
    return "Just some hot water in a cup."

class Chocolate(HotBeverage):
  Price = 0.50
  Name = "chocolate"
  def description(self):
    return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
  Price = 0.45
  Name = "cappuccino"
  def description(self):
    return "Un po' di Italia nella sua tazza!"
