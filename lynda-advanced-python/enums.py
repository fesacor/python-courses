import enum
from enum import Enum, unique

@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    #PEAR = enum.auto()

def main():
    print(Fruit.TOMATO)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    print(Fruit.APPLE.name, Fruit.APPLE.value)

    print(Fruit.PEAR.value)

if __name__ == "__main__":
    main()