from pif import PIF
from scanner import Scanner
from symboltable import SymbolTable
from utils import Utils


class Console:

    def __init__(self):
        self.finite_automata = Utils.readFromFile(file_name="FA2.in")

    def show_all(self):
        print("Everything: ")
        print(self.finite_automata)

    def show_states(self):
        print("The set of states is: ", end='')
        print(*self.finite_automata.Q, sep=", ")

    def show_alphabet(self):
        print("The alphabet is: ", end='')
        print(*self.finite_automata.E, sep=", ")

    def show_transitions(self):
        print("The transitions are: ", end='')
        print(self.finite_automata.delta)

    def show_set_initial_state(self):
        print("The initial state is: ", end='')
        print(self.finite_automata.q0)

    def show_set_final_states(self):
        print("The final set of states is: ", end='')
        print(*self.finite_automata.F, sep=", ")

    def check_DFA(self):
        print("Is DFA? ---> ", end='')
        print(self.finite_automata.is_DFA())

    def check_if_accepted(self):
        sequence = input('Read sequence: ')
        print("Is it accepted? ---> ", end='')
        self.finite_automata.is_accepted(sequence)

    @staticmethod
    def display_menu():
        print('\n')
        print('          ∞ MENU ∞')
        print('\t 01| • display everything •')
        print('\t 02| • display states •')
        print('\t 03| • display alphabet •')
        print('\t 04| • display transitions •')
        print('\t 05| • display initial state •')
        print('\t 06| • display final states •')
        print('\t 07| • check DFA •')
        print('\t 08| • check if a sequence is accepted •')
        print('\t  0| • exit •')
        print('\n')

    @staticmethod
    def display_main_menu():
        print('\n')
        print('          ∞ MENU ∞')
        print('\t 01| • scanner •')
        print('\t 02| • finite automata •')
        print('\t  0| • exit •')
        print('\n')

    def run(self):
        commands = {'1': self.show_all, '2': self.show_states, '3': self.show_alphabet, '4': self.show_transitions,
                    '5': self.show_set_initial_state, '6': self.show_set_final_states, '7': self.check_DFA,
                    '8': self.check_if_accepted}

        self.display_main_menu()
        print("Enter option: ", end='')
        main_command = input()
        print("\n")
        if main_command == '1':
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

        if main_command == '2':
            exit_when_done = False
            while not exit_when_done:
                self.display_menu()
                print("Enter option: ", end='')
                command = input()
                print("\n")

                if command in commands.keys():
                    commands[command]()
                elif command == '0':
                    exit_when_done = True
                else:
                    continue
