class State:
    def __init__(self, label, pos, is_final=False):
        self.label = label
        self.is_final = is_final
        self.pos = pos

    def __str__(self):
        s = ''
        s = 'label = ' + str(self.label) + ' is_final = ' + str(self.is_final) + ' pos = ' + str(self.pos)
        return s

    def is_final(self):
        return self.is_final

class Dfa:
    def __init__(self, Q=None, sigma=None, q0=None, F=None):
       self.Q = Q
       self.sigma = sigma
       self.delta = {}
       self.q0 = q0
       self.F = F
       self.cnt_nodes = 0

    def new_state(self, pos, is_final=False):
        self.cnt_nodes += 1
        state = State(self.cnt_nodes, pos, is_final)
        self.Q += state
        return state

    def get_pos(self, p):
        return self.Q[p].pos

    def add_transition(self, src_state, ch, dst_state):
        self.delta[src_state] = (ch, dst_state)
