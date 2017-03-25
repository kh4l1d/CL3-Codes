import socket,sys

print("")
print("Enter the multiplicand : ")
num1 = raw_input()

print("")
print("Enter the multiplier : ")
num2 = raw_input()

print("")
print("Enter the multiplicand's bit form's length : ")
num3 = raw_input()

print("")
print("Enter the multiplier's bit form's length : ")
num4 = raw_input()


numbers = num1 + "," + num2 + "," + num3 + "," + num4

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("localhost",5000))

clientsocket.send(numbers)

print("")
clientsocket.close()
