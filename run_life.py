# Import classes here and initialise objects and run methods
# This seperation will maintain your code more organised following

from dog_class import *

# Intisialise a Dog Object
max_dog_instance = Dog()

# Call the method.bark() on object

print(max_dog_instance.eat('BONE'))
print(max_dog_instance.bark())
print(max_dog_instance.fetch())
print(max_dog_instance.potty())
print(max_dog_instance.bark())
print(max_dog_instance.sleep())

print('wlak the dog home')
print(max_dog_instance.sleep())
print(max_dog_instance.sleep())
print(max_dog_instance.bark("Creepy Stranger!"))