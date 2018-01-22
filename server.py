import socket
import threading

while True:
    name = input("What do you want your name to be? ")

    lengthName = len(name)

    if lengthName > 14:
        print("The maximum character limit is 14")
        continue
    else:
        break

    

bn = "<"

an = ">"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 7000

serversocket.bind((host, port))

print("Waiting for a connection...")

fullName = bn + name + an

#queue up to 4 requests
serversocket.listen(4)

clientsocket,addr = serversocket.accept()

print("Got a connection from {} \nYou can start typing".format(addr))

print("Type 'exit' to stop the program")


#while True:
#    msg = input("Write a message: ")
#    if msg == "exit":
#        msg = "The other user  has closed the program"
#        clientsocket.send(msg.encode('ascii'))
#        serversocket.close()
#        exit()
#    clientsocket.send(msg.encode('ascii'))
#    rmsg = clientsocket.recv(1000000)
#    print(start,rmsg.decode('ascii'))

def sendMessages():
    while True:
        msg = input(fullName)
        if msg == "exit":
            #msg = "SYSTEM ALERT: Another user has closed the program"
            #clientsocket.send(msg.encode('ascii'))
            #serversocket.shutdown(socket.SHUT_RDWR)
            #serversocket.close()
            #clientsocket.shutdown(socket.SHUT_RDWR)
            #serversocket.close
            exit()

        else:
            msg = fullName + msg
            clientsocket.send(msg.encode('ascii'))

def receiveMessages():
    while True:
        rmsg = clientsocket.recv(1000000)
        rmsg = rmsg.decode('ascii')
        if rmsg == "exit":
            print("\nThis session has ended")
            #serversocket.shutdown(socket.SHUT_RDWR)
            #serversocket.close()
            #clientsocket.shutdown(socket.SHUT_RDWR)
            #serversocket.close()
            exit()
        
        else:
            print(rmsg)

def acceptConnections():
    while True:
        clientsocket2,addr2 = serversocket.accept()

        if clientsocket2 == int:
            stop()

    


thread1 = threading.Thread(target = sendMessages)
thread1.start()

thread2 = threading.Thread(target = receiveMessages)
thread2.start()

thread3 = threading.Thread(target = acceptConnections)
thread3.start

