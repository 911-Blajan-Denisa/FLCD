from hashtable import HashTable


class SymbolTable:
    def __init__(self, size):
        self.__hash_table = HashTable(size)

    def insert(self, value):
        self.__hash_table.insert(value)

    def remove(self, value):
        self.__hash_table.remove(value)

    def contains(self, value):
        return self.__hash_table.contains(value)

    def get_position(self, value):
        return self.__hash_table.get_position(value)

    def __str__(self):
        return str(self.__hash_table)
