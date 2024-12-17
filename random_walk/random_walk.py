from random import choice

class RandomWalk:
    '''Una clase para generar caminatas aleatorias.'''
    def __init__(self,num_points=5000):
        '''Inicializa los atributos de una caminata.'''
        self.num_points = num_points

        #Todos los caminos empiezan en (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        '''Determina la dirección y la distancia para un paso.'''
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 9, -2, 4, 22])
        return direction * distance #Ejemplo: Si x_direction = -1 y x_distance = 3, entonces x_step = -3.


    def fill_walk(self):
        '''Calcula todos los puntos del paseo.'''
        #Sigue dando pasos hasta que la caminata alcanza la longitud deseada.
        while len(self.x_values) < self.num_points:
            #Decide en qué dirección ir u cuánto avanzar en esa dirección.
            x_step = self.get_step()
            y_step = self.get_step()

            #Rechaza movimientos que no van a ninguna parte.
            if x_step == 0 and y_step == 0:
                continue

            #Calcula la nueva posición.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

