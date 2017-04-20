import socket,sys,sha

print("")
print("Enter password registered with Kerberos Server : ")
passwordInKerberosServer = raw_input()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("",5000))
serversocket.listen(5)

clientsocket, address = serversocket.accept()
receivedPasswordDigestInKbs = clientsocket.recv(1024)
receivedPasswordDigest = ""

while receivedPasswordDigestInKbs :
    receivedPasswordDigest = receivedPasswordDigest + receivedPasswordDigestInKbs
    receivedPasswordDigestInKbs = ""
    receivedPasswordDigestInKbs = clientsocket.recv(1024)

registeredPassword = sha.shaDigest(passwordInKerberosServer)

print("")
if registeredPassword == receivedPasswordDigest :
    print("Kerberos ticket granted !")
else :
    print("Kerberos ticket denied !")

print("")
clientsocket.close()
serversocket.close()
