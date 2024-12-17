from random import randint

class Die:
    '''Una clase que representa un solo dado.'''
    def __init__(self, num_sides = 6):
        '''Asume que el dado tiene seis caras.'''
        self.num_sides = num_sides

    def roll(self):
        '''Devuelve un valor aleatorio entre 1 y el número de caras.'''
        return randint(1,self.num_sides)