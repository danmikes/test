class Animal:
  x = 0
  name = ""

  def __init__(self, z):
    self.name = z

  def party(self):
    self.x = self.x + 1
    print(self.name, 'count', self.x)

class Dog(Animal):

  def bark(self):
    # self.party()
    print('bark')

pax = Animal('pax')
max = Dog('max')

pax.party()
max.party()
max.bark()
