from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.ticker import MaxNLocator

path = Path('sitka_weather_2018_full.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)


path_dv = Path('death_valley_2021_simple.csv')
lines_dv = path_dv.read_text().splitlines()
reader_dv = csv.reader(lines_dv)
header_row_dv = next(reader_dv)


#Obtiene fechas y temperaturas maximas de este archivo.
dates, highs_sitka, highs_dv = [], [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # Convierte la fecha
        high_sitka = int(row[8])  # Lee la temperatura máxima
        #high_dv = int(row2[3])
        if high_sitka:  # Verifica si el valor no está vacío
            highs_sitka.append(int(high_sitka))  # Convierte a entero y lo agrega a la lista
            dates.append(current_date)
            #highs_dv.append(high_dv)
        else:
            print(f"Temperatura faltante en la fecha: {current_date}")
    except ValueError as e:
        print(f"Error procesando la fila: {row}, error: {e}")

dates_dv = []
for row_dv in reader_dv:
    try:
        current_date = datetime.strptime(row_dv[2], '%Y-%m-%d')  # Convierte la fecha
        high_dv = int(row_dv[3])
        if high_dv:  # Verifica si el valor no está vacío
            dates_dv.append(current_date)
            highs_dv.append(high_dv)
        else:
            print(f"Temperatura faltante en la fecha: {current_date}")
    except ValueError as e:
        print(f"Error procesando la fila: {row}, error: {e}")

dates_recortada = dates[:364]
highs_sitka = highs_sitka[:364]
#Traza las temperaturas máximas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates_dv,highs_sitka, color='red', alpha=0.5)
ax.plot(dates_dv,highs_dv, color='blue', alpha=0.5)
ax.fill_between(dates_dv,highs_sitka,highs_dv,facecolor='blue',alpha=0.1)

#Da formato al trazado.
ax.set_title('Daily high and low temperatures Sitka, Death Valley 2018', fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=8)
ax.tick_params(axis='y',labelsize=10) #Ajusta el tamaño de fuente del eje y
ax.yaxis.set_major_locator(MaxNLocator(nbins=10)) # Ajusta el número máximo de etiquetas en el eje y
plt.show()