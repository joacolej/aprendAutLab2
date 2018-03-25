from tree import Tree
import math
import pdb

def id3_generate_tree(examples, attributes):
    # Si todos los ejemplos tienen el mismo valor -> Etiqueto con ese valor
    if proportion_examples_true(examples) == 1:
        return True
    elif proportion_examples_true(examples) == 0:
        return False

    # Si no me quedan atributos -> Etiqueto con el valor más común
    elif len(attributes) == 0:
        if proportion_examples_true(examples) > 0.5:
            return True
        else:
            return False

    # En caso contrario
    else:
        # Obtengo el atributo que mejor clasifica los ejemplo
        att = get_best_attribute(examples, attributes)
        new_attributes = list(attributes)
        new_attributes.remove(att)
        # Creo el árbol para devolver

        tree2 = Tree(att)
        for value in get_possible_values(examples, att):
            if value=='mediaDed':
                pdb.set_trace()
            ejemplos_vi = get_examples_for_value(examples, att, value)

            # Si ejemplos_vi es vacio -> Etiqueto con el valor más probable
            # Aca habria que revisar lo de valor mas probable
            if len(ejemplos_vi) == 0:
                if proportion_examples_true(examples) > 0.5:
                    tree2.add_option(value, True)
                else:
                    tree2.add_option(value, False)

            # En caso contrario -> ID3(Ejemplos_vi, Atributos - {A} )
            else:
                asd = id3_generate_tree(ejemplos_vi,new_attributes)
                tree2.add_option(value, asd)

        return tree2


def proportion_examples_true(examples):
    if len(examples) == 0:
        return 0.5
    positives = [x for x in examples if x['truth'] == True]
    return len(positives)/len(examples)

def get_examples_for_value(examples, att, value):
    return [x for x in examples if x[att] == value]

def get_best_attribute(examples, attributes):
    ret = attributes[0]
    for att in attributes:
        if get_gain(examples, att) > get_gain(examples, ret):
            ret = attribute
    return ret


def entropy(examples):
    pos_prop = proportion_examples_true(examples)
    neg_prop = 1 - pos_prop
    return - pos_prop * math.log(pos_prop) + (neg_prop) * math.log(neg_prop)

def get_gain(examples, attribute):
    total_entropy = 0
    for value in attribute:
        examples_from_value = [x for x in examples if x[attribute] == value]
        total_entropy += (len(examples_from_value)/len(examples))*entropy(examples_from_value)
    return entropy(examples) - total_entropy

def get_possible_values(examples, att):
    possible_values = set()
    for x in examples:
        possible_values.add(x[att])
    possible_list = sorted(list(possible_values))
    return possible_list
