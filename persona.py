from abc import ABCMeta, abstractmethod


class Person(object):
    __metaclass__ = ABCMeta

    def __init__(self, age, name):
        self.age = age
        self.name = name
        print("%s has been created of %s" % (self.name, self.age))

    @abstractmethod
    def speak(self): pass


class Athlete(Person):

    def __init__(self, age, name, sport):
        super().__init__(age, name)
        self.__sport = sport

    def speak(self, *words):
        for word in words:
            print("%s : %s" % (self.name, word))

    def practice_sport(self):
        print("%s : I'm going to practice" % self.name)

    def show_sport(self):
        return self.__sport


luis = Athlete(18, "Luis", "Tennis")
luis.speak("What's up!", "I'm here", "he he he")
luis.practice_sport()
print("Luis practices %s" % luis.show_sport())
