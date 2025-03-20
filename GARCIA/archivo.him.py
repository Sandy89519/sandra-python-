def contar_palabra():
    try:
        with open("GARCIA/himno.txt", "rt", enconding = "UTF-8") as him:
    con= him.read().lower()
    ocurrencias=0

    palabra = contenido.split()
    for palabra_en_texto ==palabra.lower():
        ocurrencias += 1

    if ocurrencias > 0:
        print(f"tu palabra elegida'{palbra}' aparece {ocurrencias} veces en el himno")
    else:
        print(f"tu palabra '{palabra}' no esta en el himno")
        
except FileNotFoundError:
    print(f"el archivo 'himno.txt' no se encuentra en el directorio ")

palabra = input("introduce la palabra que deseas buscar en el himno")
him(palabra)

    
  
 
         
         
    