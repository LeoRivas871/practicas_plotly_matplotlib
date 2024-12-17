import requests

#Realiza una llamada a la API y verifica la respuesta.


question = 'Que lenguaje quieres consultar?'
print(question)
response = input('python, javascript, ruby, c, java, perl, haskell, go: ')

url = f'https://api.github.com/search/repositories?q=language:{response}+sort:stars+stars:>10000'

headers = {'Accept': "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Convierte el objeto de respuesta en un diccionario.
response_dict = r.json()
print(f'Total repositories: {response_dict['total_count']}')
print(f'Complete results: {not response_dict['incomplete_results']}')

# Explora la información sobre los repositorios
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

# Examina el primer repositorio.
repo_dict = repo_dicts[0]
print(f'\nKeys: {len(repo_dict)}')



print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f'Name: {repo_dict['name']}')
    print(f'Owner: {repo_dict['owner']['login']}')
    print(f'Stars: {repo_dict['stargazers_count']}')
    print(f'Repository: {repo_dict['html_url']}')
    print(f'Created: {repo_dict['created_at']}')
    print(f'updated: {repo_dict['updated_at']}')
    print(f'Description: {repo_dict['description']}')
    print()
