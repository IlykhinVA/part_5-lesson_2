class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.__len__()
        self.__str__()

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: ' + self.name + ', количество этажей: ' + str(self.number_of_floors)


first_house = House('ЖК "Горский"', 18)
second_house = House('Домик в деревне', 2)
third_house = House('ООО "Кривые ручки"', 45)

print(len(first_house))
print(len(second_house))
print(len(third_house))
print(first_house)
print(second_house)
print(third_house)
