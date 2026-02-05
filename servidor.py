# ===== SERVIDOR (password + whitelist) =====
import os, socket

PASSWORD = "clave123"                    # <-- cámbiala
WHITELIST = ["sleep", "gedit", "python"] # <-- comandos permitidos

def listar():
    os.system("ps -eo pid,comm | head")

def iniciar(conn):
    cmd = conn.recv(100).decode().strip()
    ok = False
    for w in WHITELIST:
        if cmd == w or cmd.startswith(w + " "):
            ok = True
            break
    if ok:
        os.system(cmd + " &")
    else:
        print("Bloqueado por whitelist:", cmd)

def detener(conn):
    pid = conn.recv(20).decode().strip()
    print("Password recibida (repr):", repr(pwd))        # <-- agrega esta línea
    print("Password esperada (repr):", repr(PASSWORD)

    os.system("kill " + pid)

server = socket.socket()
server.bind(("127.0.0.1", 5000))  # para una sola PC usa ("127.0.0.1", 5000)
server.listen(5)
print("Servidor listo...")

while True:
    conn, addr = server.accept()

    # 1) Autenticación simple
    pwd = conn.recv(64).decode().strip()
    if pwd != PASSWORD:
        conn.close()
        continue

    # 2) Operación
    op = conn.recv(8).decode().strip()
    if op == "1": listar()
    elif op == "2": iniciar(conn)
    elif op == "3": detener(conn)


    conn.close()

