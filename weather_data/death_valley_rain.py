from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.ticker import MaxNLocator

path_sitka = Path('death_valley_2021_full.csv')
path_death_valley = Path('death_valley_2021_full.csv')

lines_sitka = path_sitka.read_text().splitlines()
lines_dv = path_death_valley.read_text().splitlines()

reader = csv.reader(lines_sitka)
header_row = next(reader)

reader_valley = csv.reader(lines_dv)
header_row_dv = next(reader_valley)

#Compara las lluvias del valle y de sitka
dates, sitka_rain, valley = [], [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # Convierte la fecha
        sitka = row[3]  # Lee la temperatura máxima
        if sitka:  # Verifica si el valor no está vacío
            sitka_rain.append(sitka)  # Convierte a entero y lo agrega a la lista
            dates.append(current_date)
        else:
            print(f"Temperatura faltante en la fecha: {current_date}")
    except ValueError:
        print(f'Missing data for {current_date}')



#Traza las temperaturas máximas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,sitka_rain, color='red', alpha=0.5)
#ax.plot(dates,valley, color='blue', alpha=0.5)
#ax.fill_between(dates,sitka_rain,valley,facecolor='blue',alpha=0.1)

#Da formato al trazado.
ax.set_title('Daily high and low temperatures death valley 2021', fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=8)
ax.tick_params(axis='y',labelsize=10) #Ajusta el tamaño de fuente del eje y
ax.yaxis.set_major_locator(MaxNLocator(nbins=15)) # Ajusta el número máximo de etiquetas en el eje y
plt.show()

