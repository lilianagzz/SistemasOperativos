# ===== CLIENTE =====
import socket

def enviar(op, extra=""):
    s = socket.socket()
    s.connect(("127.0.0.1", 5000))
    s.send(op.encode())
    if extra:
        s.send(extra.encode())
    s.close()

while True:
    print("1) Listar   2) Iniciar   3) Detener   0) Salir")
    op = input("Opción: ")

    if op == "1":
        enviar("1")

    elif op == "2":
        cmd = input("Comando a iniciar: ")
        enviar("2", cmd)

    elif op == "3":
        pid = input("PID a detener: ")
        enviar("3", pid)

    elif op == "0":
        break