class State:
    def __init__(self, label, pos, is_final=False):
        self.label = label
        self.is_final = is_final
        self.pos = pos

    def is_final(self):
        return self.is_final

class Dfa:
    def __init__(self, Q=None, sigma=None, delta=None, q0=None, F=None):
       self.Q = Q
       self.sigma = sigma
       self.delta = delta
       self.q0 = q0
       self.F = F
       self.cnt_nodes = 0

    def new_state(self, pos, is_final=False):
        self.cnt_nodes += 1
        return State(self.cnt_nodes, pos, is_final)
