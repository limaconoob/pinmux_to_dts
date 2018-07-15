class Intern:
  def __init__(self, name):
    if name:
      self.Name = name
    else:
      self.Name = "My name? I'm nobody, an intern, I have no name."
  def __str__(self):
    return self.Name
  class Coffee():
    def __str__(self):
      return "This is the worst coffee you ever tasted."
  def work(self):
    try:
      raise Exception()
    except Exception:
      return "I'm just an intern, I can't do that..."
  def make_coffee(self):
    return self.Coffee()
