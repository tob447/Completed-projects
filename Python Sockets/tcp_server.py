import socket,sys

buffsize=1024
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

except socket.error as e:
    print ("Failed to create a socket")
    print e


host=raw_input("Enter Target host here: ")
port=raw_input("Enter Target port here: ")

try:
    s.bind((host,int(port)))

except socket.error as e:
    print ("Failed to Connect")
    print e

s.listen(5)
s.setsockopt( socket.SOL_SOCKET,
socket.SO_REUSEADDR, 1 )


while True:
    print ("waiting for connection")
    client_sock, addr = s.accept()

    #print ("client connected from: ",addr)

    while True:
        data=client_sock.recv(buffsize)
        if not data or data.decode('utf-8') == 'END':
            break

        print data.deode("utf-8")
        break

    #client_sock.close()

s.close()
