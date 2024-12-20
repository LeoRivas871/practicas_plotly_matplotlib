import plotly.express as px
from die import Die
#Crea un D6.
die = Die()

#Hace algunas tiradas y guarda los resultados en una lista.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analiza los resultados.
frequencies = []
poss_results = range(1,die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualiza los resultados.
title = 'Results of rolling one D6 1000 times'
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x=poss_results,y=frequencies,title=title, labels=labels)
fig.show()

print(frequencies)