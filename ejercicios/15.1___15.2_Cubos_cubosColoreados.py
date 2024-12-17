import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values,c=x_values,cmap=plt.cm.Blues,s=10)

#Establece el titulo del gráfico y las etiquetas de los ejes.
ax.set_title('Square numbers', fontsize=24)
ax.set_xlabel('Value',fontsize=14)
ax.set_ylabel('Square of value',fontsize=14)

#Establece el tamaño de las etiquetas de los puntos de los ejes.
ax.tick_params(labelsize=14)

#Establece el rango para cada eje.
ax.axis([0,5100,0,125000000000])
ax.ticklabel_format(style='plain')
plt.show()