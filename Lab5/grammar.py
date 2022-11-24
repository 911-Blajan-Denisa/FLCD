class Grammar:

    def __init__(self):
        self.terminals = []
        self.nonTerminals = []
        self.startingSymbol = None
        self.productions = dict()

    def loadFromFile(self, filePath):
        separator = ','
        production_sep = '|'
        production_arrow = "->"

        try:
            file = open(filePath, "r")

            self.nonTerminals = file.readline().replace('\n', '').split(separator)
            self.terminals = file.readline().replace('\n', '').split(separator)
            self.startingSymbol = file.readline().replace('\n', '').split(separator)[0]

            production = file.readline().replace('\n', '').split(production_arrow)

            while len(production) > 1:
                tokens = production[1].split(production_sep)
                self.productions[production[0]] = tokens
                production = file.readline().replace('\n', '').split(production_arrow)

        except Exception as ex:
            print(ex)

    def isCFG(self):
        if self.startingSymbol not in self.nonTerminals:
            return False

        for lhs in self.productions.keys():
            if lhs not in self.nonTerminals:
                return False
            for rhs in self.productions[lhs]:
                for symbol in rhs.split(' '):
                    if symbol not in self.terminals and symbol not in self.nonTerminals and symbol != "EPS":
                        return False

        return True

    def printNonTerminals(self):
        print(self.nonTerminals)

    def printTerminals(self):
        print(self.terminals)

    def printStartingSymbol(self):
        print(self.startingSymbol)

    def printProductions(self):
        print(self.productions)


if __name__ == '__main__':
    g = Grammar()
    g.loadFromFile("G1.txt")
    g.printStartingSymbol()
    g.printNonTerminals()
    g.printTerminals()
    g.printProductions()
    print(g.isCFG())
