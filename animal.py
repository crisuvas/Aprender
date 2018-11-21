class Animal:
    def __init__(self):
        print("An Animal was born")

    @staticmethod
    def roar():
        print("ROAR!!!!!!!!")


class Mammal(Animal):
    def __init__(self, kind):
        super().__init__()
        self.kind = kind

    def drink(self):
        print("I am drinking %s's milk" % self.kind)


class Oviparous(Animal):
    def __init__(self, egg_form):
        super().__init__()
        self.egg_form = egg_form

    def hatch(self):
        print("The egg in form of %s has hatched" % self.egg_form)


mandrill = Mammal("Mandrill")
crocodile = Oviparous("Oval")
mandrill.roar()
crocodile.roar()
mandrill.drink()
crocodile.hatch()