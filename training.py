# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
from id3 import id3_generate, id3_generate_better, get_formatted_dataset, get_attributes_from_dataset
from evaluate import cross_validation, normal_validation, split_data
import sys
import pdb
from scipy.io import arff
import pandas as pd
from model import Model

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
dataset5 = arff.loadarff('data/autismo.arff')
df = pd.DataFrame(dataset5[0])
dataset5 = df.to_dict('records')
dataset5 = get_formatted_dataset(dataset5)
datasets[5] = dataset5

# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

	ds = datasets[int(sys.argv[1])]
	model = None

	args = len(sys.argv)
	if args == 2:
		model = Model()
		#tree = id3_generate_better(ds, attributes)
	else:
		model = Model(int(sys.argv[2]), int(sys.argv[3]))


		train, test = split_data(ds, int(sys.argv[5]), 0.8)
		if int(sys.argv[4])==0:
			normal_validation(train,test,model)
		if int(sys.argv[4])==1:
			cross_validation(10,train+test, model)



	#if type(tree) is bool:
	#	print(tree)
	#else:
	#	tree.print_tree(0)
