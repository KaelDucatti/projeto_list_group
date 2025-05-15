import urllib.request
import json


url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}"

resposta = urllib.request.urlopen(url)

dados = resposta.read()

json_dados = json.loads(dados)

print(json_dados["results"])
