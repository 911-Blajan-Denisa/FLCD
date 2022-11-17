class FiniteAutomata:

    def __init__(self, Q: list, E: list, q0, F: list, S: dict):
        self.Q = Q
        self.E = E
        self.delta = S
        self.q0 = q0
        self.F = F

    def is_DFA(self):
        for elem in self.delta.keys():
            if len(self.delta[elem]) > 1:
                return False
        return True

    def is_accepted(self, sequence):
        if self.is_DFA():
            # Start parsing the input string with the current state as start state
            current_state = self.q0

            for char in sequence:
                # Transition to the next state using the current state and input alphabet
                current_state = self.delta[(current_state, char)][0]

                # Check whether the DFA goes into a dead/rejected state
                if current_state is None:
                    print("Rejected")
                    break

            else:
                # When entire string is parsed, check whether the final state is an accepted state
                if current_state in self.F:
                    print("Accepted")
                else:
                    print("Rejected")

    def __str__(self):
        return "Q = { " + ', '.join(self.Q) + " }\n" \
               "E = { " + ', '.join(self.E) + " }\n" \
               "q0 = { " + self.q0 + " }\n" \
               "S = { " + str(self.delta) + " } " \
               "F = { " + ', '.join(self.F) + " }\n"
