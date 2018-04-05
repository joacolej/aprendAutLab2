# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
import pdb

# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

class Tree:

    # CONSTRUCTOR ---------------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    
    def __init__(self, attribute, childs = None):

        # String identifying node's attribute
        self.attribute = attribute 
        
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

    def print_tree(self):

        print (self.attribute)
        
        for key, value in self.options.items():
            print(key)
            if type(value) == Tree:
                value.print_tree()
            else:
                print(value)
