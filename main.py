# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
from id3 import id3_classify, id3_classify_better, id3_generate, id3_generate_better, get_attributes_from_dataset
import sys
import pdb

# DATA --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

datasets = [None,None,None,None,None,None,None]

# Dataset used in class
datasets[0] = [ {'dedicacion': 'alta'  ,'dificultad': 'alta',  'horario': 'nocturno', 'humedad': 'media', 'humordoc': 'bueno', 'truth': True},
                                {'dedicacion': 'baja'  ,'dificultad': 'media', 'horario': 'matutino', 'humedad': 'alta',  'humordoc': 'malo',  'truth': False},
                                {'dedicacion': 'media' ,'dificultad': 'alta',  'horario': 'nocturno', 'humedad': 'media', 'humordoc': 'malo',  'truth': True},
                                {'dedicacion': 'media' ,'dificultad': 'alta',  'horario': 'matutino', 'humedad': 'alta',  'humordoc': 'bueno', 'truth': False}
                                ]

# Dataset used an example for testing
datasets[1] = [ {'temperatura': 'calida' ,'lluvia': 'si',  'horario': 'matutino', 'truth': True},
                        {'temperatura': 'templada' ,'lluvia': 'no', 'horario': 'matutino', 'truth': True},
                        {'temperatura': 'fria' ,'lluvia': 'si',  'horario': 'nocturno', 'truth': False},
                        {'temperatura': 'calida' ,'lluvia': 'no',  'horario': 'matutino', 'truth': False},
                        {'temperatura': 'calida' ,'lluvia': 'no',  'horario': 'nocturno', 'truth': True}
                       ]

# Dataset used for testing continuous values
datasets[2] = [ {'temperatura': 10 ,'lluvia': 'si',  'horario': 'matutino', 'truth': False},
                        {'temperatura': 10 ,'lluvia': 'no',  'horario': 'matutino', 'truth': False},
                        {'temperatura': 11 ,'lluvia': 'no', 'horario': 'matutino', 'truth': False},
                        {'temperatura': 13 ,'lluvia': 'no',  'horario': 'matutino', 'truth': True},
                        {'temperatura': 14 ,'lluvia': 'si',  'horario': 'nocturno', 'truth': False},
                        {'temperatura': 17 ,'lluvia': 'si',  'horario': 'nocturno', 'truth': False},
                        {'temperatura': 20 ,'lluvia': 'no',  'horario': 'nocturno', 'truth': True},
                        {'temperatura': 21 ,'lluvia': 'si',  'horario': 'nocturno', 'truth': True},
                        {'temperatura': 21 ,'lluvia': 'no',  'horario': 'nocturno', 'truth': True},
                        {'temperatura': 22 ,'lluvia': 'no',  'horario': 'matutino', 'truth': True},
                        {'temperatura': 22 ,'lluvia': 'no',  'horario': 'nocturno', 'truth': True},
                        {'temperatura': 24 ,'lluvia': 'si',  'horario': 'matutino', 'truth': True},
                        {'temperatura': 25 ,'lluvia': 'no',  'horario': 'matutino', 'truth': False},
                        {'temperatura': 27 ,'lluvia': 'no',  'horario': 'matutino', 'truth': False},
                        {'temperatura': 27 ,'lluvia': 'no',  'horario': 'nocturno', 'truth': False}
                  ]

# Dataset used for testing missing values
datasets[3] = [  {'temperatura': 'fria' ,'lluvia': 'si',  'horario': 'nocturno', 'truth': False},
                 {'temperatura': 'calida' ,'lluvia': 'si',  'horario': 'matutino', 'truth': True},
                 {'temperatura': 'templada' ,'lluvia': 'no', 'horario': 'matutino', 'truth': True},
                 {'temperatura': '?' ,'lluvia': 'no',  'horario': 'matutino', 'truth': False},
                 {'temperatura': '?' ,'lluvia': 'no',  'horario': 'nocturno', 'truth': True}
                ]

# Dataset used for testing continuous and missing values
datasets[4] = [ {'temperatura': 10 ,'lluvia': 'si',  'horario': 'matutino', 'truth': True},
         {'temperatura': 10 ,'lluvia': 'no',  'horario': 'matutino', 'truth': False},
         {'temperatura': '?' ,'lluvia': 'no', 'horario': 'matutino', 'truth': True},
         {'temperatura': 50 ,'lluvia': 'no',  'horario': 'nocturno', 'truth': True},
         {'temperatura': 30 ,'lluvia': 'si',  'horario': 'nocturno', 'truth': False}
        ]

# Real dataset used for part C
#dataset6 = arff.loadarff('data/autismo.arff')
#df = pd.DataFrame(dataset6[0])
#dataset6 = df.to_dict('records')
#dataset6 = get_formatted_dataset(dataset6)

# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

        ds = datasets[int(sys.argv[1])]
        attributes = get_attributes_from_dataset(ds)
        tree = None

        args = len(sys.argv)
        continuous = 2
        missing = 2
        if args == 2:
                tree = id3_generate_better(ds, attributes)
        else:
                continuous = int(sys.argv[2])
                missing = int(sys.argv[3])
                tree = id3_generate_better(ds, attributes, continuous, missing)
        
        print()
        print("-> Decision tree: ")
        if type(tree) is bool:
                print(tree)
        else:
                tree.print_tree(0)

        print()
        print("-> List of attributes: ")
        print(attributes)

        text = ""

        while text != "exit":
                print()
                text = input("-> Enter an example separated by ',' to classify. Enter exit to stop the classifier:\n")

                if text != "exit":
                        values = text.split(",")
                        example = {}
                        i = 0

                        try:
                                for att in attributes:
                                        example[att] = values[i]
                                        i = i + 1
                                print(id3_classify_better(tree, example,continuous, missing))

                        except error:
                                print("The entered example does not match the amount of attributes")
                        