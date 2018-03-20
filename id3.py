from tree import Tree
import math

def id3_generate_tree(examples, attributes, cur_att):

    if proportion_examples_true(examples) == 1:
        return Tree(cur_att, True)
    elif proportion_examples_true(examples) == 0:
        return Tree(cur_att, False)
    elif not attributes:
        if proportion_examples_true(examples) > 0.5:
            return Tree(cur_att, True)
        else:
            return Tree(cur_att, False)
    else:
        att = get_best_attribute(examples, attributes)
        tree = Tree(att)
        for value in get_possible_values(att):
            ejemplos_vi = get_examples_for_value(examples, att, value)
            if not ejemplos_vi:
                if proportion_examples_true(examples) > 0.5:
                    tree.add_child(value, True)
                else:
                    tree.add_child(value, False)
            else:
                new_attributes = list(attributes)
                new_attributes.remove(att)
                tree.add_child(value,
                                id3_generate_tree(examples, new_attributes, value, att))
        return tree


def proportion_examples_true(examples):
    if len(examples) == 0:
        return 0.5
    positives = [x | x in examples and x[truth] == True]
    return len(positives)/len(examples)

def get_examples_for_value(examples, att, value):
    return [x | x in examples and x[att] == value]

def get_best_attribute(examples, attributes):
    ret = attributes[0]
    for att in attributes:
        if get_gain(examples, attribute) > get_gain(examples, ret):
            ret = attribute
    return ret


def entropy(examples):
    pos_prop = proportion_examples_true(examples)
    neg_prop = 1 - pos_prop
    return - pos_prop * math.log(pos_prop) + (neg_prop) * math.log(neg_prop)

def get_gain(examples, attribute):
    total_entropy = 0
    for value in attribute:
        examples_from_value = [x | x in examples and examples[attribute] == value]
        total_entropy += (len(examples_from_value)/len(examples))*entropy(examples_from_value)
    return entropy(examples) - total_entropy
