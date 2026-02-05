# servidor.py
import socket

HOST = '0.0.0.0'   # Escuchar en todas las interfaces de red
PORT = 65432       # Puerto para escuchar

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Recibido:", data.decode())
            mensaje = input("Escribe una respuesta: ")
            conn.sendall(mensaje.encode())