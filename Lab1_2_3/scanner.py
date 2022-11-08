import re


class Scanner:
    def __init__(self):
        self.__reserved_words = []
        self.__separators = []
        self.__operators = []
        self.read_tokens()

    def get_reserved_words(self):
        return self.__reserved_words

    def get_separators(self):
        return self.__separators

    def get_operators(self):
        return self.__operators

    def get_all(self):
        return self.__operators + self.__separators + self.__reserved_words

    def read_tokens(self):
        with open('Token.in', 'r') as f:
            f.readline()

            for i in range(9):
                separator = f.readline().strip()
                if separator == "space":
                    separator = " "
                self.__separators.append(separator)

            for i in range(13):
                self.__operators.append(f.readline().strip())

            for i in range(13):
                self.__reserved_words.append(f.readline().strip())

    def is_operator(self, elem):
        for o in self.__operators:
            if elem in o:
                return True
        return False

    @staticmethod
    def is_constant(elem):
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', elem) is not None

    @staticmethod
    def is_identifier(elem):
        return re.match(r'^[a-z]([a-zA-Z]|[0-9])*$', elem) is not None

    def get_line_tokens(self, line):
        token = ''
        tokens = []
        i = 0
        while i < len(line):
            if self.is_operator(line[i]):
                if len(token) > 0:
                    tokens.append(token)
                token = ''
                while i < len(line) and self.is_operator(line[i]):
                    token += line[i]
                    i += 1
                tokens.append(token)
                token = ''

            elif line[i] in self.__separators:
                if len(token) > 0:
                    tokens.append(token)
                token = line[i]
                i += 1
                tokens.append(token)
                token = ''

            else:
                token += line[i]
                i += 1

        if len(token) > 0:
            tokens.append(token)

        return tokens
