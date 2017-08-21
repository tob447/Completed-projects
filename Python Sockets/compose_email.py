from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

class Correo:
    #ESTA PARTE ES SOLO PARA ARMAR EL MENSAJE

    def __init__(self,s,r,a,m):
        self.recipient=r
        self.sender=s
        self.asunto=a
        self.mensaje=m

        self.servidor="smtp.gmail.com"
        self.puerto=587
        self.msg=""


    def componer(self):
        self.msg=MIMEMultipart()

        self.msg['To']=self.recipient

        self.msg['From']=self.sender

        self.msg['Subject']=self.asunto


        part=MIMEText('text','plain')

        message=self.mensaje

        part.set_payload(message)

        self.msg.attach(part)

    def adjuntar(self,direccion):
        filename=direccion
        image=MIMEImage()



    def enviar(self,passw):

        #ESTA PARTE ES PARA ENVIAR EL MENSAJE
        STMTP_SERVER=self.servidor
        SMTP_PORT=self.puerto
        password=passw

        session=smtplib.SMTP(STMTP_SERVER,SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.sender,password)
        session.sendmail(self.sender,self.recipient,self.msg.as_string())
        session.quit()
    def set_recipient(self,nuevo):
        self.recipient=nuevo

    def set_mensaje(self,nuevo):
        self.mensaje=nuevo

hola=Correo("gugusito@gmail.com","gugusito@gmail.com","hola","hola mundo que tal")

hola.componer()
hola.enviar("duradura447")
