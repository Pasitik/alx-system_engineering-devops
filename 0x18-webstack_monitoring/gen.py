import requests

API_KEY = "dbc220439888d3072800b423a9852aae"
APP_KEY = "2157ff5e88669866d9b6567d51d1128e197a7afd"

url = "https://api.datadoghq.com/api/v1/dashboard"

headers = {
    "DD-API-KEY": API_KEY,
    "DD-APPLICATION-KEY": APP_KEY
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    hosts = response.json()
    # for host in hosts:
    print(hosts)
else:
    print("Error occurred:", response.text)
