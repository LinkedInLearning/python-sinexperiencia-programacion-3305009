contactos = {
  "Ana": "(901) 166-8355",
  "Luis": "(982) 231-7357",
  "Rosa": "(831) 996-1240",
  "Sofía": "(540) 487-5928"
}

informacion_rosa = contactos.get("Rosa")
print(informacion_rosa)

claves_nombre = contactos.keys()
print(claves_nombre)

valor_telefono = contactos.values()
print(valor_telefono)

contactos.update({"Sofía": "(197) 282-8671"})
print(contactos)

contactos["Ana"] = "(708) 764-4578"
print(contactos)

contactos["Mateo"] = "(868) 659-6715"
print(contactos)

contactos.pop("Luis")
print(contactos)

for clave, valor in contactos.items():
  print(f"Nombre: {clave} Teléfono:{valor}")