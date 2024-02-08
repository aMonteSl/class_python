#!/usr/bin/python3


class Car:
    def __init__(self, brand, model, color):
        self._brand = brand  # Protect
        self.__model = model # Private
        self.color = color # Public

    def setBrand(self, brand):
        self._brand = brand

    def setModel(self, model):
        self.__model = model

    def getModel(self, model):
        return self.__model

    def showDataCar(self):
        print(f"The car of the brand {self._brand} and model {self.__model} and color {self.color}")


if __name__ == "__main__":
    car = Car(brand="Toyota", model="CHR", color="Blanco")
    car.showDataCar()

    """print(car.color)
    print(car._brand)   # Esta protegido pero es publico
    print(car.__model)"""   # Es privado no se puede tocar para nada

    # car._brand = "Renault" Esto nunca
    car.setBrand("Renault") # ASi si


    # Nunca tocar aqui los atributos de una clase, se tiene que hacer dentro del ambito de la clase

    