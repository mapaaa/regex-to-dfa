class State:
    def __init__(self, label, is_final=False):
        self.label = label
        self.is_final = is_final

    def is_final(self):
        return self.is_final

class Dfa:
    def __init__(self, q=None, sigma=None, delta=None, q0=None, f=None):
       self.q = q
       self.sigma = sigma
       self.delta = delta
       self.q0 = q0
       self.f = f
