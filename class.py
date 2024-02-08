#!/usr/bin/python3

class Person:
    numero_personas = 0


    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.ojos = 2
        Person.numero_personas += 1

    def sayHi(self):
        print(f"Hi! my name is {self.name} and i am {self.age} years old")

    @classmethod
    def giveNumberPerson(cls):
        return cls.numero_personas

    
class Worker(Person):
    def __init__(self, name, age, money):
        super().__init__(name, age)
        self.money = money

    def showData(self):
        print(f"{self.name} has {self.age} years old and has {self.money}$")

    
if __name__ == "__main__":
    adri = Person(name="Adrian", age="21")
    #print(adri.name, adri.age)
    #adri.sayHi()

    juan = Person(name="Juan", age="28")
    #print(juan.name, juan.age)
    #juan.sayHi()

    maria = Worker(name="Maria", age="35", money="1200")
    #maria.showData()
    #maria.sayHi()

    print(Person.giveNumberPerson())