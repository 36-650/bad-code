class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    if 1 > 2:
        if 2 > 3:
            print("hello")

p1 = Person("John", 36)

print(p1.name)
print(p1.age)