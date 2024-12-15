from pickle import PickleError


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
                for i in range(1, new_floor + 1):
                    if 1 <= new_floor <= self.number_of_floors:
                        print(i)
                    else:
                        print('Такого этажа не существует')
                        break
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, Количество этажей: {self.number_of_floors}'


h1 = House('ЖК Парус', 15)
h2 = House('ЖК EboLand', 69)
h1.go_to(4)
h2.go_to(70)

#__str__
print(h1)
print(h2)

#__len__
print(len(h1))
print(len(h2))



