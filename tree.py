import pdb
class Tree:

    def __init__(self, attribute, child = []):
        self.attribute = attribute
        self.tree = child

    def get_value(self):
        return value

    def set_value(self, attribute):
        self.attribute = attribute

    def add_child(self, value, child):
        self.tree.append( Tree(value,child) )

    def add_leaf(self,value,result):
        self.tree.append( Tree(value,result) )

    def is_leaf(self):
        return not isinstance(self.tree, dict)

    def print_tree(self):
        print (self.attribute)
        print(self.tree)
        if type(self.tree) == list:
            for value in self.tree:
                pass
#                print(key)
                #print(value.print_tree())
                #print(value.print_tree())
#        else:
#            print("NO ES LISTA")
#            self.tree.print_tree()
