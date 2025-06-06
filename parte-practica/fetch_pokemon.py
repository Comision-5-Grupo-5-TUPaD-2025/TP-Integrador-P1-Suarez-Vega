from requests import get, RequestException

def obtener_pokemones():#Llamamos el endpoit del listado de pokemones, estableciendo el limite de items en 1000.
  url = "https://pokeapi.co/api/v2/pokemon?limit=1000"

  try:
    respuesta = get(url, timeout=10)
    respuesta.raise_for_status()#Buscamos que respuesta arroje un error si existe.
    datos = respuesta.json()
    nombres = [p["name"] for p in datos["results"]]
   
    return sorted(nombres)#Ordenamos la lista devuelta para poder usar busqueda binaria.
  except RequestException as error:#Si respuesta tiene error, lo informamos aquí.
    print(f"Error al consultar la PokeAPI: {error}")
    return []
  
def encuentra_pokemon(pokemon):#Buscamos un pokemon especifico.
  url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

  try:
    respuesta = get(url, timeout=10)
    respuesta.raise_for_status()#Buscamos que respuesta arroje un error si existe.
    return respuesta.json()
  except RequestException as error:
    print(f"Error al recuperar los datos de {pokemon.capitalize()}: {error}")#Si respuesta tiene error, lo informamos aquí.
    return []