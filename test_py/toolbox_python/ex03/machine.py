from beverages import HotBeverage

class CoffeeMachine():
  served_coffee = 0
  def __init__(self):
    CoffeeMachine.served_coffee += 1
  class BrokenMachineException():
    def work(self):
      try:
        raise Exception()
      except Exception:
        return "This coffee machine has to be repaired."
  class EmptyCup(HotBeverage):
    Price = 0.90
    Name = "empty cup"
    def description(self):
      return "An empty cup?! Gimme my money back!"
  def repair(self):
    pass
  def serve(self):
    pass

#class Compteur:
#       objets_crees = 0
#                           def __init__(self):
#                                             Compteur.objets_crees += 1
