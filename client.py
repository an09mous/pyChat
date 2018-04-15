import socket
import os

def sendf(conn):
 conn.send(str.encode('TRIGGER'))
 path=input('Enter the path of the file you want to send: ')
 if os.path.exists(path):
  conn.send(str.encode(path))
  with open(path,'rb') as file:
   data=file.read()
   conn.send(data)
 else:
  conn.send(str.encode('UNSUCCESSFUL!'))
  print('File doesn\'t exist')
  
def recvf(conn):
 print('WAIT! Other cliet is sending a file...')
 name=os.path.basename(conn.recv(4096).decode('utf-8'))
 with open('recieved_'+name, 'wb') as file:
  file.write(conn.recv(10485790))
 print('File received successfully!')
 conn.send(str.encode('File recieved successfully!'))

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 4444))

flag=s.recv(4096).decode('utf-8')
print(flag)
flag=flag[0]
print(s.recv(4096).decode('utf-8'))
my_name=input('What\'s your name buddy?: ')
if flag=='1':
 print('You are Client 1! Send some data to 2nd client to proceed...')
 while True: 
  inp=input('{}: '.format(my_name))
  if inp !='SENDF':
   s.send(str.encode(inp))
  else:
   sendf(s)
  resp=s.recv(4096).decode('utf-8') 
  if resp !='TRIGGER':
   print('Client 2: '+resp)
  else:
   recvf(s)
else:
 print('You are Client 2! Wait for 1st client to proceed...')
 while True:
  resp=s.recv(4096).decode('utf-8')
  if resp!='TRIGGER':
   print('Client 1: '+resp)
  else:
   recvf(s)
  inp=input('{}: '.format(my_name))
  if inp!='SENDF':
   s.send(str.encode(inp))
  else:
   sendf(s)

s.close()