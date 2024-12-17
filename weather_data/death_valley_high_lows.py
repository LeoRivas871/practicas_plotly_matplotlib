from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.ticker import MaxNLocator

path = Path('death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

#Obtiene fechas y temperaturas maximas de este archivo.
dates, highs, lows = [], [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # Convierte la fecha
        high = int(row[3])  # Lee la temperatura máxima
        low = int(row[4])
        if high and low:  # Verifica si el valor no está vacío
            highs.append(int(high))  # Convierte a entero y lo agrega a la lista
            dates.append(current_date)
            lows.append(low)
        else:
            print(f"Temperatura faltante en la fecha: {current_date}")
    except ValueError:
        print(f'Missing data for {current_date}')

#Traza las temperaturas máximas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,highs, color='red', alpha=0.5)
ax.plot(dates,lows, color='blue', alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#Da formato al trazado.
ax.set_title('Daily high and low temperatures death valley 2021', fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=8)
ax.tick_params(axis='y',labelsize=10) #Ajusta el tamaño de fuente del eje y
ax.yaxis.set_major_locator(MaxNLocator(nbins=10)) # Ajusta el número máximo de etiquetas en el eje y
plt.show()

