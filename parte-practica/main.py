import time
import fetch_pokemon

pokemones = (fetch_pokemon.obtener_pokemones()) #Con la función auxiliar se obtiene una lista ordenada.
parametro = input("Ingrese el nombre de un Pokémon para buscarlo, por ejemplo 'Charmander': ")
parametro = parametro.lower()

def busqueda_binaria(pokemon):
  comienzo_ejecucion = time.time()#Tomamos el tiempo al inicio de ejecución.
  inicio = 0
  final = len(pokemones) - 1

  while inicio <= final:
    medio = (inicio + final) // 2
    if pokemon == pokemones[medio]:
      final_ejecucion = time.time()#Tomamos el tiempo al final de ejecución.
      print(f"El tiempo de ejecución de la búsqueda fue de {final_ejecucion - comienzo_ejecucion}")#Calculamos el tiempo empleado por el algoritmo.
      print(f"Se encontró el elemento a buscar, estaba en la posición {medio}")#Informamos en que posición se encuentra el medio de la búsqueda.
      return pokemones[medio]
    elif pokemon > pokemones[medio]:
      print(f"Iteración de búsqueda, el medio se encuentra en la posición {medio}")#Informamos en que posición se encuentra el medio de la búsqueda.
      inicio = medio + 1
    elif pokemon < pokemones[medio]:
      print(f"Iteración de búsqueda, el medio se encuentra en la posición {medio}")#Informamos en que posición se encuentra el medio de la búsqueda.
      final = medio - 1
    else:
      return None
  final_ejecucion = time.time()#Tomamos el tiempo al final de ejecución.
  print(f"El tiempo de ejecución de la búsqueda fue de {final_ejecucion - comienzo_ejecucion}")#Calculamos el tiempo empleado por el algoritmo.
    
def maneja_busqueda_pokemon():
  resultado = busqueda_binaria(parametro)#Con el parametro ingresado por el usuario, llamamos a la búsqueda binaria.

  if resultado is None:#Si no se encuentra el Pokémon, notificamos al usuario.
    return f"El Pokémon '{parametro.capitalize()}' no esta en la Pokedex, o el profesor todavía no lo descubre."
  else:
    pokemon_encontrado = fetch_pokemon.encuentra_pokemon(resultado)#Si se encuentra el pokémon, encuentra_pokemon() llama al endpoint individual.
    nombre = pokemon_encontrado['name'].capitalize()
    tipos = []
    for tipo in pokemon_encontrado['types']:#A veces los pokemones son de mas de un tipo, construimos un array de tipos.
     tipos.append(tipo['type']['name'])
    poderes = []
    for tipo in pokemon_encontrado['moves'][:5]:#A veces los pokemones tienen muchos poderes, construimos un array con los 5 primeros poderes que tenga.
     poderes.append(tipo['move']['name'])
    tipos = ", ".join(tipos)
    tipos = f"es de tipo: {tipos}" if len(tipos) == 1 else f"es de tipos: {tipos}"
    poderes = ", ".join(poderes)
    poderes = f"tiene este poder: {poderes}" if len(poderes) == 1 else f"tiene estos poderes: {poderes}"

    return f"¡Encontramos tu Pokémon! Se llama {nombre}, {tipos} y {poderes}"
  

print(maneja_busqueda_pokemon()) 