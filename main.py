from id3 import id3_generate_tree, get_possible_values
import pdb

data = [ {'dedicacion': 'alta'  ,'dificultad': 'alta',  'horario': 'nocturno', 'humedad': 'media', 'humordoc': 'bueno', 'truth': True},
         {'dedicacion': 'baja'  ,'dificultad': 'media', 'horario': 'matutino', 'humedad': 'alta',  'humordoc': 'malo',  'truth': False},
         {'dedicacion': 'media' ,'dificultad': 'alta',  'horario': 'nocturno', 'humedad': 'media', 'humordoc': 'malo',  'truth': True},
         {'dedicacion': 'media' ,'dificultad': 'alta',  'horario': 'matutino', 'humedad': 'alta',  'humordoc': 'bueno', 'truth': False}
        ]

#atributos = ['dedicacion', 'dificultad', 'horario', 'humedad', 'humordoc']
atributos = ['dedicacion','dificultad', 'horario', 'humedad', 'humordoc']


print('-------------------------------')
ricoArbolito = id3_generate_tree(data, atributos)
ricoArbolito.print_tree()
