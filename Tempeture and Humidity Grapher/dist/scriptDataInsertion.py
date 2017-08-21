import serial, sqlite3, time

conn=sqlite3.connect("ProyectoFinal1.db")
c=conn.cursor()
error=True
while(error):
        try:
                ser = serial.Serial('COM5', 9600)
                print("Serial Connection Succesfully stablished")
                error=False
        except serial.SerialException:
                print ("Serial Conection Failed, trying again")
        

def tableCreate():
        c.execute("CREATE TABLE Temperatura(ID INT,valor INT,Fecha TIMESTAMP)")
        c.execute("CREATE TABLE Humedad(ID INT,valor INT,Fecha TIMESTAMP)")
    
def dataEntry(tabla,valor):
        c.execute("INSERT INTO %(tabla)s (Fecha,valor) VALUES(CURRENT_TIMESTAMP,%(valor)s)"%{"tabla":tabla,
                                                                         "valor":valor})
        conn.commit()


def serialRead():
    ser = serial.Serial("/dev/ttyUSB0")
    for data in ser.readline():
        if data:
            serial=data

    return serial

def parse(toParse):
        toParse=toParse.split(" ")
        humidity=toParse[0]
        temperature=toParse[1]
        toParse=[humidity,temperature]
        return toParse
        
while True:

        temperatura=parse(ser.readline())[1]
        humedad=parse(ser.readline())[0]

        dataEntry("Temperatura",temperatura)
        dataEntry("Humedad",humedad)

        print (humedad)

        print (temperatura)
        print (contador)

                
                       
        
        
  



   
    

    
    
