import pdb
class Tree:

    def __init__(self, attribute, childs = {}):
        self.attribute = attribute
        self.options = childs

    def add_option(self,value,result):
        self.options[value] = result

    def print_tree(self):
        print (self.attribute)
        print(self.options)
        if type(self.options) == list:
            for value in self.options:
                pass
