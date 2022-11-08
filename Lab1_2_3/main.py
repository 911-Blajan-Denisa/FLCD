from pif import PIF
from scanner import Scanner
from symboltable import SymbolTable

if __name__ == '__main__':
    st = SymbolTable(6)
    pif = PIF()
    scanner = Scanner()

    program = "p1.txt"
    # program = "p1err.txt"
    exception = ""

    with open(program, 'r') as file:
        index_line = 1

        for line in file:
            tokens = scanner.get_line_tokens(line.strip())
            for i in range(len(tokens)):
                if tokens[i] in scanner.get_all():
                    if tokens[i] == ' ':
                        continue
                    pif.insert(tokens[i], -1)

                elif scanner.is_identifier(tokens[i]):
                    st.insert(tokens[i])
                    identifier = tokens[i]
                    pif.insert("identifier", st.get_position(identifier))

                elif scanner.is_constant(tokens[i]):
                    st.insert(tokens[i])
                    constant = tokens[i]
                    pif.insert("constant", st.get_position(constant))

                else:
                    exception += 'Lexical error --> ' + tokens[i] + ' -- at line ' + str(index_line) + "\n"
            index_line += 1

    with open('ST.out', 'w') as writer:
        writer.write(str(st))

    with open('PIF.out', 'w') as writer:
        writer.write(str(pif))

    if exception == '':
        print("Lexically correct!\n")
    else:
        print("Lexically incorrect!\n")
        print(exception)
