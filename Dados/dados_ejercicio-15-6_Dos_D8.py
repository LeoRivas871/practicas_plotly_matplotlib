import plotly.express as px
from die import Die
#Crea dos dados D6.
die_1 = Die(8)
die_2 = Die(8)

#Hace algunas tiradas y guarda los resultados en una lista.
results = []
for roll_num in range(150000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

#Analiza los resultados.
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2,max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualiza los resultados.
title = 'Results of rolling a D8 and a D8 50000 times'
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x=poss_results,y=frequencies,title=title, labels=labels)

#Añade personalizaciones al grafíco.
fig.update_layout(xaxis_dtick=1)
fig.show()

print(frequencies)