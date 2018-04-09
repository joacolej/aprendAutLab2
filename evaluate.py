import random
import math
from model import Model


def normal_validation(trainDs, evaluate, model):
    model.train(trainDs)
    cant, uneval = get_correct(evaluate, model)
    print ("Total: {}, Positivos: {}, Negativos: {}, Evaluacion: {}, Inevaluables: {}"
            .format(len(evaluate),
                    len([x for x in evaluate if x['truth'] == True]),
                    len([x for x in evaluate if x['truth'] == False]),
                    cant,
                    uneval))

def split_data(ds, randSeed, percentage):
    # Set random seed
    random.seed(randSeed)

    # Shuffle list in case it is ordered
    shuffled = list(ds)
    random.shuffle(shuffled)


    lenght = len(shuffled)
    cut_point = math.floor(percentage * lenght)
    return (shuffled[:cut_point], shuffled[cut_point:])

def cross_validation(k,dataset, model):
    k_partitions = []

    # Get partitions size
    partition_size = math.floor(len(dataset) / k)
    # if k is not multiple of lenght of dataset there will be elements not taken into account
    left_elements = len(dataset) - partition_size * k

    # left and right offset to include those elements
    left_offset = 0
    right_offset = 0

    for i in range(0,k):
        # i have left elements
        if left_elements > 0:
            # move the right offset
            right_offset += 1
            # one element left less to take into account (because it will be added)
            left_elements -= 1
        # append a list of elements of size partition_size and one more element if left_elements > 0
        k_partitions.append( list(dataset[i+left_offset:i+partition_size+right_offset]) )
        # move the left offset
        left_offset = right_offset

    evaluation = 0
    uneval = 0
    for i in range(0,k-1):
        join = list(filter(lambda x: x not in k_partitions[i],dataset))

        # se entrena el modelo
        classifier = model.train(join)

        # evaluo
        cant, uneval = get_correct(join, model)
        evaluation += cant
        uneval += uneval

    print ("Total: {}, Positivos: {}, Negativos: {}, Evaluacion: {}, Inevaluables: {}"
            .format(len(dataset),
                    len([x for x in dataset if x['truth'] == True]),
                    len([x for x in dataset if x['truth'] == False]),
                        evaluation/k,
                        uneval))


def get_correct(examples, model):
    cant = len(examples)
    corrects = 0
    unevaluable = 0
    for example in examples:
        result = model.classify(example)
        if result == None:
            cant = cant -1
            unevaluable += 1
        else:
            if  result == example['truth']:
                corrects += 1
    return (corrects / cant, unevaluable)
