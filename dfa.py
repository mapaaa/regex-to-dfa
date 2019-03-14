class State:
    def __init__(self, label, is_final=False):
        self.label = label
        self.is_final = is_final

    def is_final(self):
        return self.is_final
