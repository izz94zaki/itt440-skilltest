import socket

host='izani.synology.me'
port= 8443

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

message = '2021470892'
s.sendall(message.encode('utf-8'))

data = s.recv(1024)

s.close()

print(data.decode('utf-8'))
