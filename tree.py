class Data:
    def __init__(self, operator=None, operand=None, label=None):
        self.operator = operator
        self.operand = operand
        self.label = label

class Node:
    def __init__(self, left=None, right=None):
        self.left = None
        self.right = None
        self.data = None
