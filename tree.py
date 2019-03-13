class Data:
    def __init__(self, operator=None, operand=None, label=None, ind=None):
        self.operator = operator
        self.operand = operand
        self.label = label
        self.ind = ind
        self.nullable = None
        self.first_pos = []
        self.last_pos = []

class Node:
    def __init__(self, left=None, right=None):
        self.left = None
        self.right = None
        self.data = None

    def is_leaf(self):
        return (self.left == None and self.right == None)

    def get_operand(self):
        return self.data.operand

    def get_ind(self):
        return self.data.ind

    def get_nullable(self):
        return self.data.nullable

    def get_first_pos(self):
        return self.data.first_pos

    def get_last_pos(self):
        return self.data.last_pos
