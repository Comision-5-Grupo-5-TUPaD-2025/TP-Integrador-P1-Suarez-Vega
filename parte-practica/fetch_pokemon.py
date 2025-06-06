from requests import get, RequestException

def obtener_pokemones():
  url = "https://pokeapi.co/api/v2/pokemon?limit=1000"

  try:
    respuesta = get(url, timeout=10)
    respuesta.raise_for_status()
    datos = respuesta.json()
    nombres = [p["name"] for p in datos["results"]]
   
    return sorted(nombres)
  except RequestException as error:
    print(f"Error al consultar la PokeAPI: {error}")
    return []
  
def encuentra_pokemon(pokemon):
  url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

  try:
    respuesta = get(url, timeout=10)
    respuesta.raise_for_status()
    return respuesta.json()
  except RequestException as error:
    print(f"Error al recuperar los datos de {pokemon.capitalize()}: {error}")
    return []