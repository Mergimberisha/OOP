# Abstract and create the class dog

class Dog():

    # This is a special method
    # It comes defined either way but we can re-write it
    # This method stands for initialise class object AKA the constructor in other languages
    # Allows us to set attributes to our Dog objects
        # ... Like.. the poor thing doesn't even have a name:(
            # We should give it a name... possible Max :)

        # Refers to the instance of the object
    def __index__(self):
        self.name = 'Mad Max'


# This is a method that can be used by a dog instance
    def bark(self, person = ''):
        return 'woof, woof! I see you there' + ' ' + person

    def bark_print(self):
        return 'woof, woof!'

    def eat(self, food):
        return 'Nom, nom, nom, nom!' + ' ' + food.lower()

    def sleep(self):
        return 'zzZZzzZZz, ZZzzzZZzz!'

    def fetch(self):
        return "WHERE THAT BALL AT? --- I'ma get that ball!!"

    def potty(self):
        return "UHHHH!!! AHAHHH! 0_o UUHHH!! ..... O_O .. :) o.o .."

# Initialising a Dog Object
dog_instance1 = Dog()

# This print should not be here.
# In this file you define the class dog and add attributes and method to the class
# That is it.
# print(dog_instance1)
# print(type(dog_instance1))