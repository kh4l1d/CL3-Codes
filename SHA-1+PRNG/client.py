import socket,sys,sha

print("")
print("Enter your password to gain a Kerberos ticket : ")
password = raw_input()

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("localhost",5000))

passwordDigest = sha.shaDigest(password)
clientsocket.send(passwordDigest)

print("")
clientsocket.close()
