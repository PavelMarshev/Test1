class Car:
    def __init__(self, name):
        self.car_name = name

    def print_result(self):
        print(self.car_name)


class Plane:
    def __init__(self, name):
        self.plane_name = name

    def print_result(self):
        print(self.plane_name)


class Factory:
    @staticmethod
    def create_car(name):
        return Car(name)

    @staticmethod
    def create_plane(name):
        return Plane(name)


Factory.create_car('bmw').print_result()



