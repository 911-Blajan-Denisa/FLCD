from grammar import Grammar
import copy


class Parser:

    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.firstTable = dict()
        self.followTable = dict()
        self.eps = "EPS"

    def initTable(self, table: dict, doFollow=False):
        for nonTerminal in self.grammar.nonTerminals:
            table.update({nonTerminal: set()})
        if doFollow:
            table[self.grammar.startingSymbol].add(self.eps)

    def first(self):
        previous_table = dict()
        self.initTable(previous_table)
        self.initTable(self.firstTable)

        done = False
        while not done:
            for nonTerminal in self.firstTable.keys():
                for production in self.grammar.productions[nonTerminal]:
                    production_first = production.split(" ")[0]
                    if production_first in self.grammar.terminals or production_first == self.eps:
                        self.firstTable[nonTerminal].add(production_first)
                    else:
                        if self.eps not in previous_table[production_first]:
                            self.firstTable[nonTerminal].update(previous_table[production_first])
                        else:
                            i = 0
                            while self.eps in previous_table[production_first]:
                                self.firstTable[nonTerminal].update(previous_table[production_first])
                                i = i + 1
                                if i >= len(production.split(" ")):
                                    break
                                production_first = production.split(" ")[i]

            if self.firstTable == previous_table:
                done = True
            previous_table = copy.deepcopy(self.firstTable)

    def follow(self):
        previous_follow = dict()
        self.initTable(previous_follow, True)
        self.initTable(self.followTable, True)

        done = False
        while not done:
            for nonTerminal in self.followTable.keys():
                for production in [item for sublist in self.grammar.productions.values() for item in sublist]:
                    tokens = production.split(" ")
                    if nonTerminal in tokens:
                        if nonTerminal == tokens[-1]:
                            self.followTable[nonTerminal].add(self.eps)
                            break
                        start = False
                        for token in tokens:
                            if start:
                                if token in self.grammar.terminals:
                                    self.followTable[nonTerminal].add(token)
                                    break
                                self.followTable[nonTerminal].update(self.firstTable[token])
                                if self.eps not in self.firstTable[token]:
                                    break
                            if token == nonTerminal:
                                start = True
            if previous_follow == self.followTable:
                done = True
            previous_follow = copy.deepcopy(self.followTable)


if __name__ == '__main__':
    g = Grammar()
    g.loadFromFile("G1.txt")
    p = Parser(g)
    p.first()
    print(p.firstTable)
    p.follow()
    print(p.followTable)
