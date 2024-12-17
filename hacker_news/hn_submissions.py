import plotly.express as px
from operator import itemgetter
import requests

# Hace una llamada a la API y guarda la respuesta.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

# Procesa la información sobre cada envío.
submission_ids = r.json()
submission_dicts = []
comments = []
links = []
titles = []

for submission_id in submission_ids[:30]:
    # Hace una nueva llamada a la API separada para cada envío.
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)

    if r.status_code == 200:
        response_dict = r.json()
        try:
            # Crea un diccionario para cada artículo.
            submission_dict = {
                'title': response_dict['title'],
                'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
                'comments': response_dict['descendants'],
            }
            submission_dicts.append(submission_dict)
            titles.append(response_dict['title'])
            links.append(submission_dict['hn_link'])
            comments.append(response_dict['descendants'])
        except KeyError:
            print(f'Skipping submission {submission_id} due to missing fields.')
# Ordena las historias por número de comentarios en orden descendente.
sorted_data = sorted(zip(titles, comments, links), key=lambda item: item[1], reverse=True)
titles, comments, links = zip(*sorted_data)

# Crea la gráfica de barras.
fig = px.bar(x=titles, y=comments, title='Most Commented Posts on Hacker News', labels={'x': 'Posts', 'y': 'Number of Comments'})

# Añade los enlaces como anotaciones HTML.
fig.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=list(range(len(titles))),
        ticktext=[f'<a href="{link}" target="_blank">{title}</a>' for title, link in zip(titles, links)]
    )
)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()
