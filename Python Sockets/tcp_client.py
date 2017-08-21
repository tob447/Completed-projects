import socket,sys
from threading import Thread

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

except socket.error as e:
    print ("Failed to create a socket")
    print e

host="192.168.0.105"#raw_input("Enter Target host here: ")
port=12345#raw_input("Enter Target port here: ")

try:
    s.connect((host,int(port)))

except socket.error as e:
    print "Error Connecting"
    print e

print ("Connected to host: %s and port: %s" %(host,port))

def leer():
    while True:
        data=s.recv(1024)
        print data.decode("utf-8")


def send():
    while True:
        payload=raw_input("Enter here text to send: ")
        s.send(payload)

if __name__=="__main__":
    t1=Thread(target=leer)
    t2=Thread(target=send)
    t1.daemon=True
    t2.daemon=True
    t1.start()
    t2.start()
