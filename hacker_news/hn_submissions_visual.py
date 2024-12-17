import requests
import plotly.express as px

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

response_dict = r.json()
print(f'Total de id´s: {len(response_dict)}')

sites_list = []
submission_dicts = []
comments = []
titles = []
for re_dict in response_dict[:10]:
    sites = f"https://hacker-news.firebaseio.com/v0/item/{re_dict}.json"
    r = requests.get(sites)
    if r.status_code == 200:
        response_dict = r.json()
        try:
            diccionario ={
                'title': response_dict['title'],
                'hn_link': f'https://news.ycombinator.com/item?id={re_dict}',
                'comments': response_dict['descendants'],
            }
            submission_dicts.append(diccionario)
            titles.append(diccionario['title'])
            sites_list.append(diccionario['hn_link'])
            comments.append(diccionario['comments'])
        except KeyError:
            pass


#Ordenar los datos en orden descendente según el numero de comentarios
sorted_data = sorted(zip(comments, sites_list), reverse=True)
sorted_comments, sorted_sites_list = zip(*sorted_data)

#Visualización
title = 'Discuciones más populares'
labels = {'x': 'Sites', 'y':'Comments'}
fig = px.bar(x=list(sorted_sites_list),y=list(sorted_comments),title=title,labels=labels)

fig.update_layout(
    xaxis=dict(
        tickmode='array',
        ticktext=[f'<a href="{link}" target="_blank"><a/>' for link in sorted_sites_list],
        tickvals=list(sorted_sites_list)
    )
)

fig.show()