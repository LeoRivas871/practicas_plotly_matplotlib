import python_repos
import requests

response = 'python'

url = f'https://api.github.com/search/repositories?q=language:{response}+sort:stars+stars:>10000'

headers = {'Accept': "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

def test_status_code():
    a = r.status_code
    assert a == 200