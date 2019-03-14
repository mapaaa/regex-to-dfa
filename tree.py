class Data:
    def __init__(self, operator=None, operand=None, label=None, ind=None):
        self.operator = operator
        self.operand = operand
        self.label = label
        self.ind = ind
        self.nullable = None
        self.first_pos = []
        self.last_pos = []

    def show(self):
        s = ''
        if self.operator:
            s += ' operator = ' + str(self.operator)
        if self.operand:
            s += ' operand = ' + str(self.operand)
        s += ' label = ' + str(self.label)
        s += ' ind = ' + str(self.ind)
        s += ' nullable = ' + str(self.nullable)
        s += ' first_pos = ' + str(self.first_pos)
        s += ' last_pos = ' + str(self.last_pos)
        return s

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.data = None

    def __str__(self):
        s = ''
        s = self.data.show() #super unsafe
        return s

    def is_leaf(self):
        return (self.left == None and self.right == None)

    def get_operator(self):
        return self.data.operator

    def get_ind(self):
        return self.data.ind

    def get_nullable(self):
        return self.data.nullable

    def get_first_pos(self):
        return self.data.first_pos

    def get_last_pos(self):
        return self.data.last_pos
