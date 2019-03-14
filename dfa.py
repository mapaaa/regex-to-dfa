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
    def __init__(self, sigma=None, q0=None):
       self.Q = []
       self.sigma = sigma
       self.delta = {}
       self.q0 = q0
       self.F = []
       self.cnt_nodes = 0

    def __str__(self):
        s = 'Q = ['
        for state in self.Q:
            s += str(state) + ', '
        s += ']\n'
        s += 'sigma = ' + str(self.sigma) + '\n'
        s += 'q0 = ' + str(self.q0.label) + '\n'
        s += 'F = ' + str(self.F)
        return s

    def new_state(self, pos, is_final=False):
        self.cnt_nodes += 1
        state = State(self.cnt_nodes, pos, is_final)
        self.Q.append(state)
        if is_final == True:
            self.F.append(state)
        return state

    def get_pos(self, p):
        return self.Q[p].pos

    def add_transition(self, src_state, ch, dst_state):
        self.delta[src_state] = (ch, dst_state)

    def is_state_already(self, pos_state):
        for state in self.Q:
            if set(state.pos) == set(pos_state):
                return True
        return False

    def get_state(self, p):
        return self.Q[p]
