class HashTable:
    def __init__(self, size: int) -> None:
        self.__table = [[] for _ in range(size)]
        self.__size = size

    def contains(self, elem):
        return elem in self.__table[self.hash(elem)]

    def hash(self, key: str) -> int:
        suma = 0
        for character in key:
            suma += ord(character)
        return suma % self.__size

    def insert(self, value):
        if not self.contains(value):
            key = self.hash(value)
            self.__table[key].append(value)

    def remove(self, value):
        key = self.hash(value)
        self.__table[key].remove(value)

    def get_position(self, value):
        key = self.hash(value)
        return self.hash(value), self.__table[key].index(value)

    def __str__(self) -> str:
        representation = ""
        for i in range(self.__size):
            representation += str(i) + " -> " + str(self.__table[i]) + "\n"
        return representation
