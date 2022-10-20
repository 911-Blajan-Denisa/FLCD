class LexicInserter:

    def __init__(self):
        self.separators = []
        self.operators = []
        self.reserved_words = []
        self.classify()

    def classify(self) -> None:
        with open('token.txt', 'r') as f:
            f.readline()
            for i in range(10):
                separator = f.readline().strip()
                if separator == "space":
                    separator = " "
                self.separators.append(separator)
            for i in range(11):
                self.operators.append(f.readline().strip())
            for i in range(8):
                self.reserved_words.append(f.readline().strip())
