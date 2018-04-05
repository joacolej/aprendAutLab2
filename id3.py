
# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
from tree import Tree
import math
import pdb

# MAIN METHODS ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Using a dataset "ds" of training examples and a list "attributes" of attributes, generates a decision tree using ID3
def id3_generate(ds, attributes):

    # Border Case: Every example is labeled true
    # Returns true (dont care if is root or not, ID3 is recursive)
    if proportion_examples_true(ds) == 1:
        return True

    # Border Case: Every example is labeled false
    # Returns false (dont care if is root, ID3 is recursive)
    elif proportion_examples_true(ds) == 0:
        return False

    # Border Case: There are no more attributes
    # Returns the most likely value between true and false
    elif len(attributes) == 0:
        if proportion_examples_true(ds) > 0.5:
            return True
        else:
            return False

    # No Border Case
    else:

        # 1. Get the attribute that best classifies ds (highest information gain)
        att = get_best_attribute(ds, attributes)
        #print (att)

        # Aux: Delete the chosen attribute, it will not be used in further iterations
        new_attributes = list(attributes)
        new_attributes.remove(att)

        # 2. Create an empty dictionary which will have the children nodes for the tree (booleans or nodes)
        options = {}

        # 3. Iterate through the possible values for "att" in "ds"
        for value in get_possible_values(ds, att):

            # 3.1. Get a list of examples that match value "value" in attribute "att"
            examples_vi = get_examples_for_value(ds, att, value)

            # 3.2. If there are no examples for the value, the answer is the most likely value between true and false
            if len(examples_vi) == 0:
                if proportion_examples_true(ds) > 0.5:
                    options[value]= True
                else:
                    options[value] = False

            # 3.3. If there are still examples for the value, triggers recursive execution
            # This time using the set of examples with value "value" in "att" as dataset
            # and excluding "att" from the list of attributes
            else:
                node = id3_generate(examples_vi, new_attributes)
                options[value] = node

        # 4. Create and return the tree node
        return Tree(att, options)

# Using a decision tree "tree", classifies a valid example
def id3_classify(tree, attributes):
    return False

# AUXILIAR METHODS --------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Given a dataset "ds" of training examples, returns a list of each attribute names
def get_attributes_from_dataset(ds):

    attributes = []

    for example in ds:
        for key in list(example.keys()):
            if key not in attributes and key != 'truth':
                attributes.append(str(key))

    return attributes

# Given a dataset "ds" of training examples, returns the proportion of the ones labeled as positive
def proportion_examples_true(ds):
    if len(ds) == 0:
        return 0.5
    positives = [x for x in ds if x['truth'] == True]
    return len(positives) / len(ds)

# Given a dataset "ds" and a list "attributes", returns the attribute that gives the highest information gain
def get_best_attribute(ds, attributes):
    ret = attributes[0]
    for att in attributes:
        if get_gain(ds, att) > get_gain(ds, ret):
            ret = att
    return ret

# Given a dataset "ds" and an attribute "att", returns the information gain in "ds" for "attribute"
def get_gain(ds, att):
    entropia = 0
    cant_ejemplos = len(ds)

    for value in get_possible_values(ds,att):
        subset = get_examples_for_value(ds, att, value)
        entropia += ((len(subset)/cant_ejemplos) * entropy(subset))

    return entropy(ds) - entropia

# Given a dataset "ds" and an attribute "attribute", returns the possibles values for "attribute" in "ds"
def get_possible_values(ds, att):
    possible_values = set()

    for x in ds:
        possible_values.add(x[att])

    return sorted(list(possible_values))

# Given a dataset "ds", an attribute "att" and a value "value", returns the list of examples in "ds" which have value "value" for attribute "att"
def get_examples_for_value(examples, att, value):
    return [x for x in examples if x[att] == value]

# Given a dataset "ds", returns the entropy for the set of examples
def entropy(ds):
    pos_prop = proportion_examples_true(ds)
    neg_prop = 1 - pos_prop
    if pos_prop == 0 or neg_prop == 0:
        return 0
    entropia = - pos_prop * math.log(pos_prop,2) - neg_prop * math.log(neg_prop,2)
    return entropia
