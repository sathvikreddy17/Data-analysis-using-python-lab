def __init__(self, name):
 self.name = name
 def speak(self):
 return "Some generic animal sound"
 def move(self):
 return "The animal moves around"
class cat(Animal):
 def speak(self):
return f"{self.name} says: Meow! Meow!"
 def move(self):
 return f"{self.name} runs quietly."
cat = cat("cutie")
animals = [cat]
for animal in animals:
 print(animal.speak())
 print(animal.move())
