# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
from id3 import id3_generate, id3_generate_better, get_attributes_from_dataset
import sys
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
dataset2 = [ {'temperatura': 'calida' ,'lluvia': 'si',  'horario': 'matutino', 'truth': True},
         {'temperatura': 'templada' ,'lluvia': 'no', 'horario': 'matutino', 'truth': True},
         {'temperatura': 'fria' ,'lluvia': 'si',  'horario': 'nocturno', 'truth': False},
         {'temperatura': 'calida' ,'lluvia': 'no',  'horario': 'matutino', 'truth': False},
         {'temperatura': 'calida' ,'lluvia': 'no',  'horario': 'nocturno', 'truth': True}
        ]

dataset3 = [ {'temperatura': 10 ,'lluvia': 'si',  'horario': 'matutino', 'truth': True},
         {'temperatura': 40 ,'lluvia': 'no',  'horario': 'matutino', 'truth': False},
         {'temperatura': 20 ,'lluvia': 'no', 'horario': 'matutino', 'truth': True},
         {'temperatura': 50 ,'lluvia': 'no',  'horario': 'nocturno', 'truth': True},
         {'temperatura': 30 ,'lluvia': 'si',  'horario': 'nocturno', 'truth': False}
        ]

dataset4 = [ {'clima': 'calido' ,'lluvia': 'si',  'horario': 'matutino', 'truth': True},
         {'clima': 'templado' ,'lluvia': 'no', 'horario': 'matutino', 'truth': True},
         {'clima': 'frio' ,'lluvia': 'si',  'horario': 'nocturno', 'truth': False},
         {'clima': 'calido' ,'lluvia': 'no',  'horario': 'matutino', 'truth': False}
        ]


# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

	ds = dataset3
	attributes = get_attributes_from_dataset(ds)
	tree = None

	args = len(sys.argv)
	if args == 1:
		tree = id3_generate_better(ds, attributes)
	else:
		tree = id3_generate_better(ds, attributes, int(sys.argv[1]), int(sys.argv[2]))
	
	if type(tree) is bool:
		print(tree)
	else:
		tree.print_tree(0)
