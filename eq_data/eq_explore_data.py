from pathlib import Path
import json
import plotly.express as px

#Lee los datos como una cadena y lo convierte en un objeto python.
path = Path('eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#Analiza todos los terremotos del conjunto de datos.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

#Extraer magnitudes y datos de ubicación.
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])


'''Mapa'''
title = all_eq_data['metadata']['title']
fig = px.scatter_geo(lat=lats,lon=lons,size=mags,title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     ) #Representar magnitudes
fig.show()