class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year


    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    def drive(self):
        print(f'Car {self.__model} is driving.')

    def __str__(self):
        return f'MODEL: {self.model}, YEAR: {self.year}'

class FuelCar(Car):
    def __init__(self, model, year):
        super().__init__(model, year)
        self.__fuel_bank = fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.__fuel_bank} is driving by fuel.')

    def __str__(self):
        


#some_car = Car('Ford', '2021')
#print(some_car)


