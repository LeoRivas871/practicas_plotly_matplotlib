import matplotlib.pyplot as plt
from random_walk.random_walk import RandomWalk

#Sigue generando caminatas mientras el programa esté activo.
while True:
    #Crea una caminata aleatoria.
    rw = RandomWalk(5000)
    rw.fill_walk()

    #Traza los puntos de la caminata.
    plt.style.use('classic')
    fig,ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values,rw.y_values,linewidth='1')
    ax.set_aspect('equal')
    #Enfatizar el primer punto y el último.
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #Elimina los ejes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    #print(rw.x_values)
    #print(rw.y_values)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break


