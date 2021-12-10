#Stephanie M. Ramos Camacho


#libreria a importar
import time
import random
import socket
import sys


#un ID diferente que se le asigna al proceso, el "IP address" del "compute server",
#y el numero de "port" del "compute server".
mobileID = sys.argv[1]
localHost = sys.argv[2]
port = int(sys.argv[3])

jobMax = 16

#cuando hace el mensaje de trabajo de CPU con el numero del mobile
def msjMobile(mobileID):
	job = random.randrange(1, jobMax)
	msj = "%s : %s" % (mobileID, job)
	return msj


while True:
	sockete = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sockete.sendto(msjMobile(mobileID).encode(), (localHost, port))
	time.sleep(random.randrange(1, 5))

#Mobile 3 consumed 204 seconds of CPU time