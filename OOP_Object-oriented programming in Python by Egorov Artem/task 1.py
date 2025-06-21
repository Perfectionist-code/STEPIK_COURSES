from typing import Protocol


class Animal(Protocol):
    def walk(self) -> None:
        ...

    def speak(self) -> None:
        ...


class Dog:
    def walk(self) -> None:
        print("This is a dog walking")

    def speak(self) -> None:
        print("Woof!")


def make_animal_speak(animal: Animal) -> None:
    animal.speak()


dog = Dog()
make_animal_speak(dog)