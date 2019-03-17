class State:
    def __init__(self, label, pos, is_final=False):
        self.label = label
        self.is_final = is_final
        self.pos = pos

    def __str__(self):
        s = ''
        s = 'label = ' + str(self.label) + ' is_final = ' + str(self.is_final) + ' pos = ' + str(self.pos)
        return s

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
        s += 'F = ' + '\n'
        for state in self.F:
            s += '-->' + str(state) + '\n'
        s += 'delta = ' + '\n'
        for (src, value) in self.delta.items():
            for dst in value:
                s += '-->' + str(src) + ', ' + str(dst[0]) + ' -> ' + str(dst[1])
                s += '\n'
        return s


    # custom output format for graphviz_web
    def str_graphviz_web_format(self):
        s = ''
        for (src, value) in self.delta.items():
            for dst in value:
                for a in src.pos:
                    s += str(a)
                s += ' -> '
                for a in dst[1].pos:
                    s += str(a)
                s += ' [label=' + str(dst[0]) + ', fontsize=18]'
                s += '\n'
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
        if src_state in self.delta:
            self.delta[src_state].append((ch, dst_state))
        else:
            self.delta[src_state] = [(ch, dst_state)]


    def is_state_already(self, pos_state):
        for state in self.Q:
            if set(state.pos) == set(pos_state):
                return True
        return False


    def search_state(self, pos_state):
        for state in self.Q:
            if set(state.pos) == set(pos_state):
                return state


    def get_state(self, p):
        return self.Q[p]
