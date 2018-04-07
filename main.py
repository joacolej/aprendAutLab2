# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
from probabilistic_id3 import id3_classify, id3_generate, get_attributes_from_dataset
from probabilistic_id3 import classify
import pdb

# DATA --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Dataset used in class
dataset1 = [ {'dedicacion': 'alta'  ,'dificultad': 'alta',  'horario': 'nocturno', 'humedad': 'media', 'humordoc': 'bueno', 'truth': True},
             {'dedicacion': 'baja'  ,'dificultad': 'media', 'horario': 'matutino', 'humedad': 'alta',  'humordoc': 'malo',  'truth': False},
             {'dedicacion': 'media' ,'dificultad': 'alta',  'horario': 'nocturno', 'humedad': 'media', 'humordoc': 'malo',  'truth': True},
             {'dedicacion': 'media' ,'dificultad': 'alta',  'horario': 'matutino', 'humedad': 'alta',  'humordoc': 'bueno', 'truth': False}
           ]


# Dataset used an example for testing
dataset2 = [ {'clima': 'calido',   'lluvia': 'si',  'horario': 'matutino', 'truth': True},
             {'clima': 'templado', 'lluvia': 'no',  'horario': 'matutino', 'truth': True},
             {'clima': 'frio',     'lluvia': 'si',  'horario': 'nocturno', 'truth': False},
             {'clima': 'calido',    'lluvia': 'no', 'horario': 'matutino', 'truth': False}
           ]


# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    attributes = get_attributes_from_dataset(dataset2)
    tree = id3_generate(dataset2, attributes)
    #tree.print_probabilistic_tree(1)
    print (classify(tree, {'clima': '?' ,'lluvia': 'si',  'horario': 'nocturno', 'truth': True}))
