from datetime import datetime
import functools


class Human:
    def __init__(self, name: str):
        self.name = name
        self.money = 0

    def __str__(self):
        return f'I am {self.name}'

    # def __repr__(self):
    #     return f'Human {self.name}'
    __repr__ = __str__


class Player:
    def __init__(self, name: str, skills: list[str]):
        super().__init__()
        self.name = name
        self.skills = skills


class SportTeam:
    def __init__(self, name: str):
        self.name = name
        self.date = datetime.now()
        self.players: list[Player] = []
        self.money = 0
        self.month_salary = 1000

    def __str__(self):
        return f'Team {self.name}, \nDate: {self.date}, \nPlayers: {self.players}'

    # def __repr__(self):
    #     return f'Human {self.name}'
    __repr__ = __str__

    def pay_salary(self):
        if len(self.players) * self.month_salary <= self.money:
            print('paying......')
            for player in self.players:
                player.money += self.month_salary
                self.money -= self.month_salary

        else:
            print('No money')

    def fire(self, player: Player):
        self.players.remove(player)


team = SportTeam('Desna')
maxim2 = Player(name='Max', skills=['soccer'])
team.players.append(maxim2)
# maxim = Human('Max')
# team.players.append(maxim)
# team.pay_salary()
# team.money += 5000
# team.pay_salary()
#
# john = Human('John')
# team.players.append(john)
# team.pay_salary()
#
# print(id(team))
# print(team.money)
# print(team.players)

class Car:
    def __init__(
            self,
            year: int = 2020,
            manufacturer: str = 'Unknown',
            model: str = 'Unknown',
            fuel_consumption: float = 0.0
    ):
        self.manufacturer = manufacturer
        self.model = model
        self.mileage = 0
        self.year = year
        self.fuel_consumption = fuel_consumption
        self.write_log()

    def write_log(self):
        file_name = 'cars.csv'
        with open(file_name, mode='a', encoding='utf-8') as file:
            file.write(f'{self.manufacturer};{self.model}\n')

    def __str__(self):
        return (f"{self.year} {self.manufacturer} {self.model}, "
                f"пробіг: {self.mileage} км, витрата палива: {self.fuel_consumption} л/100км")

    # def __repr__(self):
    #     return f'Human {self.name}'
    __repr__ = __str__


class Truck(Car):
    def __init__(self, year, manufacturer, model, fuel_consumption, carrying_capacity: int = 0):
        super().__init__(year, manufacturer, model, fuel_consumption)
        self.carrying_capacity = carrying_capacity

    def __str__(self):
        return super().__str__() + f", вантажопідйомність: {self.carrying_capacity} т"


class SportCar(Car):
    def __init__(self, year, manufacturer, model, fuel_consumption, max_speed: int = 0, price: int = 0):
        super().__init__(year, manufacturer, model, fuel_consumption)
        self.max_speed = max_speed
        self.price = price

    def __str__(self):
        return super().__str__() + f", швидкість: {self.max_speed} км/г, ціна: $ {self.price}"


car1 = Car(2019, "Toyota", "Corolla", 5.6)
car2 = Car(2021, "Tesla", "Model S", 0.0)
car3 = Car(2015, "Ford", "Mustang", 8.5)

truck = Truck(2019, "Toyota", "Corolla", 5.6, 20)

sport_car = SportCar(2019, "Toyota", "Corolla", 5.6, 300, 100000)

car1.mileage = 10000
car3.mileage = 1
print(car1)
print(car2)
print(car3)
print(truck)
print(sport_car)
