# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
from id3 import id3_generate, get_attributes_from_dataset
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
dataset2 = [ {'clima': 'calido' ,'lluvia': 'si',  'horario': 'matutino', 'truth': True},
         {'clima': 'templado' ,'lluvia': 'no', 'horario': 'matutino', 'truth': True},
         {'clima': 'frio' ,'lluvia': 'si',  'horario': 'nocturno', 'truth': False},
         {'clima': 'calido' ,'lluvia': 'no',  'horario': 'matutino', 'truth': False}
        ]




# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

	attributes = get_attributes_from_dataset(dataset1)
	print(attributes)
	print()
	tree = id3_generate(dataset1, attributes)
	
	if type(tree) is bool:
		print(tree)
	else:
		tree.print_tree()
