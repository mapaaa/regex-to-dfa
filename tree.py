class Data:
    def __init__(self, operator, operand, label):
        self.operator = operator
        self.operand = operand
        self.label = label

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
