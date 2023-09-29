equipaje = ("camisa","zapatos", "pantalón", "zapatos","vestido", "calcetines", "zapatos")

cantidad_zapatos = equipaje.count("zapatos")
print(cantidad_zapatos)

primeros_zapatos = equipaje.index("zapatos")
print(primeros_zapatos)

for prenda in equipaje:
  print(prenda)