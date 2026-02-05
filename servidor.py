# ===== SERVIDOR =====
import os, socket

def listar():
    os.system("ps -eo pid,comm | head")

def iniciar():
    cmd = conn.recv(100).decode()
    os.system(cmd + " &")

def detener():
    pid = conn.recv(20).decode()
    os.system("kill " + pid)

server = socket.socket()
server.bind(("0.0.0.0", 5000))
server.listen(1)
print("Servidor listo...")

while True:
    conn, addr = server.accept()
    op = conn.recv(10).decode()

    if op == "1": listar()
    elif op == "2": iniciar()
    elif op == "3": detener()

    conn.close()