# cliente.py
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	while True:
		mensaje = input("Escribe un mensaje:")
		s.sendall(mensaje.encode())
		data = s.recv(1024)
		print('Recibido del servidor:', data.decode())