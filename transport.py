from abc import ABCMeta, abstractmethod


class Transport:
    __metaclass__ = ABCMeta

    def __init__(self, by):
        self.by = by

    @abstractmethod
    def move(self, phrase): pass

    @staticmethod
    def turn_left():
        return "Turn left!"

    @staticmethod
    def turn_right():
        return "Turn right!"

    @abstractmethod
    def stop(self): pass


class Train(Transport):
    def __init__(self, by="Train"):
        super().__init__(by)

    def move(self, phrase):
        return "It moves %s mpg an hour" % phrase

    def stop(self):
        return "It has stopped with the driver body"


class Airplane(Transport):
    def __init__(self, by="Airplane"):
        super().__init__(by)

    def move(self, phrase):
        return "It flies %s mpg an hour" % phrase

    def stop(self):
        return "It cannot be stopped"


chevy = Train()
ferrari = Airplane()
print(chevy.move(899))
print(ferrari.move(1200))
print(chevy.stop())
print(ferrari.stop())
print(ferrari.turn_left())
