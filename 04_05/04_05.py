tareas = [ "barrer el piso", "lavar los platos", "lavar la ropa", "cocinar", "limpiar los muebles"]

for tarea in tareas:
    if tarea == "lavar la ropa":
        print(f"Realizaremos esta tarea de {tarea} durante el fin de semana.")
        continue  
    print("Tarea completa:", tarea)
