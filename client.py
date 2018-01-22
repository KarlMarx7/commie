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

fullName = "\n" + bn + name + an

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 7000

s.connect((host, port))

print("Got a connection from {}".format(host))

print("Type 'exit' to stop the program")

#receive no more than 1 million bytes
#while True:
#    msg = s.recv(1000000)
#    msg = msg.decode('ascii')
#    if msg == "The other user has closed the program":
#        print("SYSTEM MESSAGE: The other user has closed the program")
#
#    print(start,msg)
#    sends = input("Write a message: ")
#    if sends == "exit":
#        sends = "The other user has closed the program"
#        s.send(sends.encode("ascii"))
#        s.close()
#        exit()
#    s.send(sends.encode("ascii"))

def receiveMessages():
    while True:
        msg = s.recv(1000000)
        msg = msg.decode('ascii')
        if msg == "exit":
            print("\nThis session has ended")
            #s.shutdown(socket.SHUT_RDWR)
            #s.close()
            exit()
        print(msg)

def sendMessages():
    while True:
        sends = input(fullName)
        if sends == "exit":
            sends = "The other user has closed the program"
            s.send(sends.encode("ascii"))
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            exit()
        else:
            sends = fullName + sends
            s.send(sends.encode("ascii"))

thread1 = threading.Thread(target = sendMessages)
thread1.start()

thread2 = threading.Thread(target = receiveMessages)
thread2.start()