class HashTable:
    def __init__(self, size):
        self.size = size
        self.__table = [[] for _ in range(self.size)]

    def contains(self, elem):
        return elem in self.__table[self.hash(elem)]

    def insert(self, key):
        if self.contains(key):
            raise Exception("The key already exists!")
        self.__table[self.hash(key)].append(key)

    def remove(self, key):
        index = self.hash(key)
        self.__table[index].remove(key)

    def hash(self, elem):
        suma = 0
        for character in elem:
            suma += ord(character)
        return suma % self.size

    def __str__(self) -> str:
        representation = ""
        for i in range(self.size):
            representation += str(i) + ": " + str(self.__table[i]) + "\n"
        return representation
