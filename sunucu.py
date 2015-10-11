import socket

host = "127.0.0.1"
port = 34000
buf = 1024
calistir = (host,port)

bagla = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
bagla.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
bagla.bind(calistir)
bagla.listen(5)

istemci,adres = bagla.accept()
print "Baglanti Geldi:",adres[0]

while True:
	data = istemci.recv(buf)
	if data == "q":
		break
	elif len(data) == 0:
		pass
	else:
		print data



istemci.close()
bagla.close()