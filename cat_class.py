# Abstract and create the class cat

class Cat():

    # This is a special method
    # It comes defined either way but we can re-write it
    # This method stands for initialise class object AKA the constructor in other languages
    # Allows us to set attributes to our Dog objects
        # ... Like.. the poor thing doesn't even have a name:(
            # We should give it a name... possible Max :)

        # Refers to the instance of the object
    def __index__(self):
        self.name = 'Calm Cax'


# This is a method that can be used by a dog instance
    def speak(self, person = ''):
        return 'meow, meow! I see you there' + ' ' + person

    def eat(self, food):
        return 'Nom, nom, nom, nom!' + ' ' + food.lower()

    def sleep(self, talk = ''):
        return 'zzZZzzZZz, ZZzzzZZzz!' + ' ' + talk

    def fetch(self, catch):
        return "WHERE THAT STRING AT? --- I'ma get that string!!" + ' ' + catch.upper()

    def potty(self):
        return "UHHHH!!! AHAHHH! 0_o UUHHH!! ..... O_O .. :) o.o .."

    def naughty(self, bad = ''):
        return "AHHHHH! I ate my owners homework!!!" + ' ' + bad.upper()

# Initialising a Cat Object
cat_instance1 = Cat()