from id3 import get_attributes_from_dataset, id3_generate_better, id3_classify_better

class Model:
    def __init__(self,continuousOption= 2, missingOption = 2):
        self.missingOption = missingOption
        self.continuousOption = continuousOption
        self.model = None

    def train(self, dataset):
        attributes = get_attributes_from_dataset(dataset)
        self.model = id3_generate_better(dataset, attributes, self.continuousOption, self.missingOption)

    def classify(self,example):
        classification = id3_classify_better(self.model, example, self.continuousOption, self.missingOption)
        if type(classification) == str:
            return None
        (x , y) = classification
        if x > y:
            return True
        else:
            return False
