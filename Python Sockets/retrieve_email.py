import poplib

class Bandeja:

    def __init__(self,user,passw):
        self.server='pop.googlemail.com'
        self.puerto="995"

        self.user=user
        self.passw=passw


        self.bandeja=poplib.POP3_SSL(self.server,self.puerto)
        self.bandeja.user(self.user)
        self.bandeja.pass_(self.passw)

    def ver_correos(self):

        listac=self.bandeja.list()

        for i in listac:
            print i

    def numero_correos(self):
        return len(self.bandeja.list()[1])# el numero 1 significa bandeja principal


    def descargar(self,numero):
        for i in self.bandeja.retr(numero)[1]:
            print i


b1=Bandeja("gugusito@gmail.com","duradura447")
b1.ver_correos()

#print b1.numero_correos()
#b1.descargar(b1.numero_correos())
