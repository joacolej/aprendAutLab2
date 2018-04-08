import random
import math


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

    for i in range(0,k,partition_size):
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
    for i in range(0,k):
        no_eval_example = list(dataset).remove(dataset[i])
        join = reduce(lambda: x,y: x+y, no_eval_example)

        # necesitamos ver como hacer esto en general
        # se entrena el modelo
        classifier = model.train(join)

        # evaluo
        evaluation += get_correct(dataset[i], classifier)


    return evaluation/k


get_correct(examples, classifier):
    cant = len(examples)
    corrects = 0
    for example in range(0, cant):
        if classifier.classify(example) == example['truth']:
            corrects += 1
    return corrects / cant
