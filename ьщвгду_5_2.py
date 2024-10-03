class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floor = floors



    def go_to(self, new_floor):
        # print('Я на 1 этаже ЖК')
        if 1 <= new_floor <= self.number_of_floor:
            for floor in range (1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует!')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

