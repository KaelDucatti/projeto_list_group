import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["API_KEY"]


url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}"

resposta = requests.get(url)

dados = resposta.json()

print(dados["results"])
