# ===== MIDDLEWARE SIMPLE =====
servidores = [
    ("192.168.1.10", 5000),
    ("192.168.1.11", 5000)
]

print("Servidores disponibles:")
for i, s in enumerate(servidores):
    print(i, s)

sel = int(input("Elegir servidor: "))
HOST, PORT = servidores[sel]

# Cliente igual, pero usando HOST, PORT