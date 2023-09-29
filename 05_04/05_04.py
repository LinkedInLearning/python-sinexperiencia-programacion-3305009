invitados = {"Luis", "Ana", "Sebastián", "Sofía", "Mateo", "Valeria"}
print(invitados)

invitados.add("Isabel")
print(invitados)

invitados.remove("Sebastián")
print(invitados)

invitados.discard("Valeria")
print(invitados)

invitado = invitados.pop()
print(invitado)
print(invitados)