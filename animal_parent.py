class Animal_parent:

    def __init__(self, name="john", age="", limbs=4):
        self.name = name
        self.age = age
        self.limbs = limbs


    def sleep(self):
        return 'I am sleeping zzzzzz'

    def eat(self):
        return 'yum! that was delicious'


    def run(self):
        return 'I am so fast'