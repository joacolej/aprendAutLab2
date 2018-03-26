from id3 import id3_generate_tree, get_possible_values
import pdb

data = [ {'dedicacion': 'altaDed'  ,'dificultad': 'altaDif',  'horario': 'nocturno', 'humedad': 'media', 'humordoc': 'bueno', 'truth': True},
         {'dedicacion': 'bajaDed'  ,'dificultad': 'mediaDif', 'horario': 'matutino', 'humedad': 'alta',  'humordoc': 'malo',  'truth': False},
         {'dedicacion': 'mediaDed' ,'dificultad': 'altaDif',  'horario': 'nocturno', 'humedad': 'media', 'humordoc': 'malo',  'truth': True},
         {'dedicacion': 'mediaDed' ,'dificultad': 'altaDif',  'horario': 'matutino', 'humedad': 'alta',  'humordoc': 'bueno', 'truth': False}
        ]

#atributos = ['dedicacion', 'dificultad', 'horario', 'humedad', 'humordoc']
atributos = ['dedicacion','dificultad', 'horario', 'humedad', 'humordoc']


print('-------------------------------')
ricoArbolito = id3_generate_tree(data, atributos)
ricoArbolito.print_tree()
