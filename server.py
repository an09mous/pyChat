import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 4444))
s.listen(3)
conn=['','']
print('Waiting for client to connect...')
for i in range(0,2):
 conn[i], addr=s.accept()
 print('{} client connected: {}'.format(i+1, addr[0]))
 conn[i].send(str.encode('{} clients connected'.format(i+1)))

conn[1].send(str.encode('Wait for 1 client to send data...'))
conn[0].send(str.encode('2 Clients Connected!, Send some data: '))
while True:
 data0= conn[0].recv(4096)
 if data0.decode('utf-8')!='TRIGGER':
  conn[1].send(data0)
 else:
  conn[1].send(data0)
  data0= conn[0].recv(4096)
  conn[1].send(data0)
  rcvfile=conn[0].recv(10485790)
  conn[1].send(rcvfile)

 data1= conn[1].recv(4096)
 if data1.decode('utf-8')!='TRIGGER':
  conn[0].send(data1)
 else:
  conn[0].send(data1)
  data1= conn[1].recv(4096)
  conn[0].send(data1)
  rcvfile=conn[1].recv(10485790)
  conn[0].send(rcvfile)
  

s.close()

