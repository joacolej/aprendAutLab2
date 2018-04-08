# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
import pdb

# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

class Tree:

    # CONSTRUCTOR ---------------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    
    def __init__(self, attribute, childs = None, most_likely = None):

        # String identifying node's attribute
        self.attribute = attribute 
        
        # String with most likely value for tree's attribute
        # It is used when a new example comes with missing value 
        self.most_likely = most_likely

        # Dictionary with keys from attribute's options
        # If is not leaf, values are children nodes,
        # Else, values are booleans giving the answer
        if childs is None:
            self.options = {}
        else:
            self.options = childs


    # MAIN METHODS --------------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------

    # Adds a "result" with key "option" to options dictionary
    # If option is to be a leaf, result is a boolean. Else, it is a child node
    def add_option(self, option, result):
        self.options[option] = result

    # Returns the value for "option", could be an answer or a child node
    def get_option(self, option):
        return self.options[option]


    # AUXILIAR METHODS ----------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------

    def print_tree(self, n):

        for x in range(0,n):
            print ('-', end="")
        print (self.attribute)
        
        for key, value in self.options.items():
            
            (node,p) = value

            for x in range(0, n+1):
                print ('-', end="")

            if p == -1:
                print(key)
            else:
                print((key,p))

            if type(node) == Tree:
                node.print_tree(n+2)
            else:
                for x in range(0, n+2):
                    print('-', end="")
                print(node)
                
