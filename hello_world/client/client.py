import requests


base_url = 'http://localhost:5000'

url = base_url+'/'
response = requests.get(url=url)
print(f'Response from GET {url}: {response.content}')

url = base_url+'/my_route'
response = requests.get(url=base_url+'/my_route')
print(f'Response from GET {url}: {response.content}')

url = base_url+'/test_post'
response = requests.post(url=url, data='Hello world, this is some data')
print(f'Response from POST {url}: {response.content}')