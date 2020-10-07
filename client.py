import socket
import threading
from utility import encodeMessage,decodeMessage

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_ADDR='localhost'
PORT=4444
server.connect((IP_ADDR,PORT))

def main():
	r=threading.Thread(target=recieve)
	s=threading.Thread(target=send)
	r.start()
	s.start()
	r.join()
	s.join()
	server.close()

def recieve():
	while True:
		try:
			msg=decodeMessage(server.recv(4096))
			print(msg)
		except:
			print('Failed to connect to server!')
			break

def send():
	while True:
		try:
			msg=encodeMessage(input())
			server.send(msg)
		except:
			print('Failed to connect to server!')
			break
if __name__ == '__main__':
	main()