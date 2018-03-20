class Tree:
    attribute = ''
    tree = {}

    def __init__(self, attribute, child = {}):
        self.attribute = attribute
        self.tree = child


    def get_value(self):
        return value

    def set_value(self, attribute):
        self.attribute = attribute

    def add_child(self, value, child):
        self.tree[value] = child

    def is_leaf(self):
        return not isinstance(self.tree, dict)
