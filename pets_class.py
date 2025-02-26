from abc import ABC, abstractmethod
import time
import random


class Pet(ABC):
    def __init__(self, hunger, happiness, energy, name):
        self.__hunger = hunger
        self.__happiness = happiness
        self.__energy = energy
        self.__name = name

    @property
    def hunger(self):
        return self.__hunger

    @hunger.setter
    def hunger(self, value):
        if value > 100:
            print('Hunger cannot be above 100.')
            self.__hunger = 100
        elif value < 0:
            print('Hunger cannot be below 0.')
            self.__hunger = 0
        else:
            self.__hunger = value

    @property
    def happiness(self):
        return self.__happiness

    @happiness.setter
    def happiness(self, value):
        if value > 100:
            print('Happiness cannot be above 100.')
            self.__happiness = 100
        elif value < 0:
            print('Happiness cannot be below 0.')
            self.__happiness = 0
        else:
            self.__happiness = value

    @property
    def energy(self):
        return self.__energy

    @happiness.setter
    def energy(self, value):
        if value > 100:
            print('Energy cannot be above 100.')
            self.__energy = 100
        elif value < 0:
            print('Energy cannot be below 0.')
            self.__energy = 0
        else:
            self.__energy = value

    def feed(self):
        self.hunger -= 20
        self.energy += 10

    def play(self):
        self.happiness += 15
        self.energy -= 10

    def sleep(self):
        self.energy += 20
        self.hunger += 10

    def show_status(self):
        print(f'{self.__name} is {self.__hunger} hungry, {self.__happiness} happy, and {self.__energy} energized.')

    def random_event(self):
        event = random.randrange(10)
        if event == 4:
            self.hunger -= 10
            print('Pet finds a snack.')
        if event == 1:
            self.happiness += 10
            print('Pet plays alone.')
        if event == 8:
            self.energy -= 10
            print('Pet has a bad dream.')

    @abstractmethod
    def special_ability(self):
        pass


class Dog(Pet):
    def __init__(self, hunger, happiness, energy, name):
        super().__init__(hunger, happiness, energy, name)

    def play(self):
        self.happiness += 20
        self.energy -= 10

    def special_ability(self):
        if self.happiness >= 80:
            self.hunger -= 10
        else:
            print('Stat is not high enough')


class Cat(Pet):
    def __init__(self, hunger, happiness, energy, name):
        super().__init__(hunger, happiness, energy, name)

    def sleep(self):
        self.energy += 30
        self.hunger += 5

    def special_ability(self):
        if self.energy <= 20:
            self.energy += 15
        else:
            print('Stat is not high enough')


class Dragon(Pet):
    def __init__(self, hunger, happiness, energy, name):
        super().__init__(hunger, happiness, energy, name)

    def feed(self):
        self.hunger -= 30
        self.energy += 15
        self.happiness += 10

    def play(self):
        self.happiness += 25
        self.hunger += 10
        self.energy -= 5

    def special_ability(self):
        if self.happiness >= 70:
            self.hunger -= 5
            self.energy += 5
        else:
            print('Stat is not high enough')


def main():

    pet_type = input('Enter the pet type you want (1.Cat, 2.Dog, 3.Dragon): ')
    user_in = input('Enter your pets name: ')

    while True:
        if pet_type == '1':
            pet = Cat(name=user_in, energy=50, happiness=50, hunger=50)
            break
        elif pet_type == '2':
            pet = Dog(name=user_in, energy=50, happiness=50, hunger=50)
            break
        elif pet_type == '3':
            pet = Dragon(name=user_in, energy=50, happiness=50, hunger=50)
            break
    time.sleep(1)

    while True:
        pet.random_event()
        pet.show_status()
        time.sleep(1)
        choice = input(
            '1.Feed \n2.Play \n3.Sleep \n4.Special Ability \n5.Exit \nChoose option: ')
        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            pet.special_ability()
        elif choice == '5':
            exit()


if __name__ == '__main__':
    main()
