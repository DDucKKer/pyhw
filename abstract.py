from abc import ABC, abstractmethod


class RequiredForAirborn(ABC):
    @abstractmethod
    def fly(self):
        pass

    def scream(self):
        print('Yo-ho')


class RequiredFuel(ABC):
    @abstractmethod
    def refuelling(self):
        pass


class AvatarCreatureAlive(RequiredForAirborn):
    def fly(self):
        # raise NotImplemented
        print('Fly')


class AvatarDrones(RequiredForAirborn, RequiredFuel):
    def fly(self):
        print('Fly')

    def refuelling(self):
        print('Refuelling')


creature = AvatarCreatureAlive()
creature.fly()
drone = AvatarDrones()
drone.scream()


class AbcDB(ABC):
    @abstractmethod
    def get_data(self, data: dict):
        pass

    @abstractmethod
    def save_data(self, data: dict):
        pass


class Mongo(AbcDB):
    TOKEN = 'data_mongo.txt'

    def get_data(self, data: dict):
        with open(self.TOKEN, 'r', encoding='utf-8') as db:
            for line in db.readlines():
                if str(data['name']) in line:
                    return line

    def save_data(self, data: dict):
        with open(self.TOKEN, 'a', encoding='utf-8') as db:
            db.write(str(data) + '\n')


class GraphQL(AbcDB):
    TOKEN = 'dkjh999999999gkjdfhdjkgb'
    URL = 'kjdfhgjkdfhgkf'


entrypoint = Mongo()

entrypoint.save_data({'name': 557})
print(entrypoint.get_data({'name': 557}))
