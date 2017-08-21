import imaplib

class Bandeja2:

    def __init__(self,user,passw):
        self.server='pop.googlemail.com'
        self.puerto="995"

        self.user=user
        self.passw=passw


        self.bandeja=imaplib.IMAP4_SSL(self.server,self.puerto)
        self.bandeja.login(self.user,self.passw)
        bandeja.select("inbox")

    def ver_correos(self):

        listac=self.bandeja.list()

        for i in listac:
            print i

    def numero_correos(self):
        return len(self.bandeja.list()[1])# el numero 1 significa bandeja principal


    def descargar(self,numero):
        for i in self.bandeja.retr(numero)[1]:
            print i
