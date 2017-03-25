import socket,sys,booths


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("",5000))
serversocket.listen(5)

clientsocket, address = serversocket.accept()
receivedNumbersInKbs = clientsocket.recv(1024)
receivedNumbers = ""

while receivedNumbersInKbs :
    receivedNumbers = receivedNumbers + receivedNumbersInKbs
    receivedNumbersInKbs = ""
    receivedNumbersInKbs = clientsocket.recv(1024)

numberList = receivedNumbers.split(',')

multiplicand = int(numberList[0])
multiplier = int(numberList[1])
multiplicandLength = int(numberList[2])
multiplierLength = int(numberList[3])


product = booths.booth(multiplicand,multiplier,multiplicandLength,multiplierLength)

print("")
print("The product of " + str(multiplicand) + " and " + str(multiplier) + " is = " + str(product))
print("")
clientsocket.close()
serversocket.close()
