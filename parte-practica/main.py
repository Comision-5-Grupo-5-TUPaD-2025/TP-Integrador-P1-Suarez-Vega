import time
import fetch_pokemon

pokemones = (fetch_pokemon.obtener_pokemones())
parametro = input("Ingrese el nombre de un Pokémon para buscarlo, por ejemplo 'Charmander': ")
parametro = parametro.lower()

def busqueda_binaria(pokemon):
  comienzo_ejecucion = time.time()
  inicio = 0
  final = len(pokemones) - 1

  while inicio <= final:
    medio = (inicio + final) // 2
    if pokemon == pokemones[medio]:
      final_ejecucion = time.time()
      print(f"El tiempo de ejecución de la búsqueda fue de {final_ejecucion - comienzo_ejecucion}")
      print(f"Se encontró el elemento a buscar, estaba en la posición {medio}")
      return pokemones[medio]
    elif pokemon > pokemones[medio]:
      print(f"Iteración de búsqueda, el medio se encuentra en la posición {medio}")
      inicio = medio + 1
    elif pokemon < pokemones[medio]:
      print(f"Iteración de búsqueda, el medio se encuentra en la posición {medio}")
      final = medio - 1
    else:
      return None
  final_ejecucion = time.time()
  print(f"El tiempo de ejecución de la búsqueda fue de {final_ejecucion - comienzo_ejecucion}")
    
def maneja_busqueda_pokemon():
  resultado = busqueda_binaria(parametro)

  if resultado is None:
    return f"El Pokémon '{parametro.capitalize()}' no esta en la Pokedex, o el profesor todavía no lo descubre."
  else:
    pokemon_encontrado = fetch_pokemon.encuentra_pokemon(resultado)
    nombre = pokemon_encontrado['name'].capitalize()
    tipos = []
    for tipo in pokemon_encontrado['types']:
     tipos.append(tipo['type']['name'])
    poderes = []
    for tipo in pokemon_encontrado['moves'][:5]:
     poderes.append(tipo['move']['name'])
    tipos = ", ".join(tipos)
    tipos = f"es de tipo: {tipos}" if len(tipos) == 1 else f"es de tipos: {tipos}"
    poderes = ", ".join(poderes)
    poderes = f"tiene este poder: {poderes}" if len(poderes) == 1 else f"tiene estos poderes: {poderes}"

    return f"¡Encontramos tu Pokémon! Se llama {nombre}, {tipos} y {poderes}"
  

print(maneja_busqueda_pokemon()) 