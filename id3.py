
# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
from tree import Tree
import math
import operator
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
def id3_classify(tree, example):
    
    # 1. Choose the current attribute in the tree
    current_att = tree.attribute

    # 2. Get the value in the example for the current attribute
    example_att = example[current_att]
    
    # 3. Get the subtree for that value
    branch = tree.options[example_att]
    if type(branch) == Tree:
        # If it is a tree, recursive call using subtree as root
        return id3_classify(branch, example)
    else:
        # Otherwise, the branch is the answer
        return branch

# Using a dataset "ds" of training examples and a list "attributes" of attributes, generates a decision tree using ID3
# This version of ID3 adds an strategy for continuous and missing values. The arguments "continuousOption" and "missingOption"
# are for choosing which strategy will be used. There are 2 and 3 possible values for each respectively:
# -------------------------------------------------------------------------------------------------------------------------
# Continuous 0: Splits the continuous range in intervals based on when the result function changes its value, adding a branch for each one
# Continuous different than 0: Does not support continuous values
# -------------------------------------------------------------------------------------------------------------------------
# Missing 0: Adds to the missing values the most likely value in the current dataset for that attribute
# Missing 1: Adds a probability to each branch of the attribute if it has missing values, which will be used to classify
# Missing different than 0,1: Does not support empty values
# -------------------------------------------------------------------------------------------------------------------------
def id3_generate_better(ds, attributes, continuousOption = 1, missingOption = 2):

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

        # 0. Fill missing values if option determines so
        if missingOption == 0:
            fill_missing_values(ds, attributes)

        # 1. Get the attribute that best classifies ds (highest information gain)
        att = get_best_attribute(ds, attributes, continuousOption == 0)

        # Aux: Delete the chosen attribute, it will not be used in further iterations
        new_attributes = list(attributes)
        new_attributes.remove(att)

        # 2. Create an empty dictionary which will have the children nodes for the tree (booleans or nodes)
        options = {}

        # 3. Get possible values for "att" in "ds"
        possible_values = []
        if continuousOption == 0 and get_continuity(ds, att):
            possible_values = get_possible_continuous_values(ds, att)
        else:
            possible_values = get_possible_values(ds, att)

        # 4. Iterate through them
        for value in possible_values:

            # 4.1. Get a list of examples that match value "value" in attribute "att"
            examples_vi = []
            if continuousOption == 0 and get_continuity(ds, att):
                examples_vi = get_examples_for_interval(ds, att, value, possible_values)
            else:
                examples_vi = get_examples_for_value(ds, att, value)

            # 4.2. If there are no examples for the value, the answer is the most likely value between true and false
            if len(examples_vi) == 0:
                if proportion_examples_true(ds) > 0.5:
                    options[value]= True
                else:
                    options[value] = False

            # 4.3. If there are still examples for the value, triggers recursive execution
            # This time using the set of examples with value "value" in "att" as dataset
            # and excluding "att" from the list of attributes
            else:
                
                node = id3_generate(examples_vi, new_attributes)
                options[value] = node

        # 5. Create and return the tree node
        return Tree(att, options)

# AUXILIAR METHODS PART B -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Checks if "att" is continuous in "ds"
def get_continuity(ds, att):

    for x in ds:
       if x[att] != '?':
            if type(x[att]) == int or type(x[att]) == float:
                return True
            else:
                return False 

# Given a dataset "ds" and a continuous attribute "att", splits att's domain into intervals based on the changes in the 
# result function, returning them as discrete values
def get_possible_continuous_values(ds, att):
    
    sorted_ds = sorted(ds, key=operator.itemgetter(att))

    possible_values = []
    old_res = None
    old_x = None

    for x in sorted_ds:

        res = x['truth']
        if old_res != None and res != old_res:
            mid = ((x[att] - old_x) / 2) + old_x
            possible_values.append(mid)

        old_res = res
        old_x = x[att]

    possible_values.append("bigger")

    return possible_values

# Given a dataset "ds", a continuous attribute "att" and an interval "interval", returns the list of examples in "ds" 
# which are between interval
def get_examples_for_interval(examples, att, interval, intervals):

    index = intervals.index(interval)
    if index == 0:
        return [x for x in examples if x[att] <= interval]
    elif interval != "bigger":
        return [x for x in examples if x[att] <= interval and x[att] > intervals[index-1]]
    else:
        return [x for x in examples if x[att] > intervals[index-1]]

# Checks if "att" has missing values in "ds"
def get_missing(ds, att):

    for x in ds:
        if x[att] == '?':
            return True
        
    return False 

# Given a dataset "ds" fills every missing value with the most likely value for that attribute
def fill_missing_values(ds, attributes):
    for att in attributes:
        if get_missing(ds,att):
            set_most_likely_value(ds, att)

# Given a dataset "ds" and an attribute "att" with missing values, fills them with the most likely value of "att" in "ds"
def set_most_likely_value(ds, att):

    values = get_possible_values(ds, att)
    most_likely = ''
    count = 0
    
    for value in values:
        large = len([x for x in ds if x[att] == value])
        if (large) > count:
            most_likely = value
            count = large

    for example in ds:
        if example[att] == '?':
            example[att] = most_likely

# Given a dataset "ds" and an attribute "att" with missing values, returns a list composed by examples with that value missing
def get_unknown_examples_for_value(ds,att):
    return [x for x in ds if x[att] == '?']

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
def get_best_attribute(ds, attributes, continuous = False):
    ret = attributes[0]
    for att in attributes:
        isContinuous = get_continuity(ds,att) and continuous
        if get_gain(ds, att, isContinuous) > get_gain(ds, ret, isContinuous):
            ret = att
    return ret

# Given a dataset "ds" and an attribute "att", returns the information gain in "ds" for "attribute"
# If isContinuous is true, takes into account that att is continuous and gets its intervals
def get_gain(ds, att, isContinuous = False):
    entropia = 0
    cant_ejemplos = len(ds)

    possible_values = []
    if isContinuous:
        possible_values = get_possible_continuous_values(ds,att)
    else:
        possible_values = get_possible_values(ds,att)

    for value in possible_values:
        subset = get_examples_for_value(ds, att, value)
        entropia += ((len(subset)/cant_ejemplos) * entropy(subset))

    return entropy(ds) - entropia

# Given a dataset "ds" and an attribute "att", returns the possibles values for "attribute" in "ds"
def get_possible_values(ds, att):
    possible_values = set()

    for x in ds:
        possible_values.add(x[att])

    possible_values.discard('?')

    return sorted(list(possible_values))

# Given a dataset "ds", an attribute "att" and a value "value", returns the list of examples in "ds" which have value "value" for attribute "att"
def get_examples_for_value(examples, att, value):
    return [x for x in examples if x[att] == value]

# Given a dataset "ds", returns its entropy
def entropy(ds):
    pos_prop = proportion_examples_true(ds)
    neg_prop = 1 - pos_prop
    if pos_prop == 0 or neg_prop == 0:
        return 0
    entropia = - pos_prop * math.log(pos_prop,2) - neg_prop * math.log(neg_prop,2)
    return entropia
