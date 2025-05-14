from car.car_1 import Car  # импортируем наследуемый класс (имя пакета -> имя модуля -> имя класса)


class ElectroCar(Car):
    def __init__(self, brand, model, year, mileage, power):
        super().__init__(brand, model, year, mileage)
        self.power = power

    def get_battery(self):
        print(f"Этот автомобиль имеет мощность {self.power} %")