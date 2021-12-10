#Stephanie M. Ramos Camacho

#libreria a importar
import threading
import time
import socket
import sys

msjMax = 30

#el total de mensajes recibidos
N = 20

#para hacer el primer thread; declarando los mensajes y el queue
x = []
queueVacio = threading.Semaphore(msjMax)
queueLleno = threading.Semaphore(0)
mutex = threading.Semaphore(1)


port = int(sys.argv[1])
sockete = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockete.bind(("localhost", port))


#producer, quien pone los "jobs" en el standard queue
def producer():
	
	while True:

		msjs, localHost = sockete.recvfrom(1024)

		mensaje = msjs.decode()
		mensaje = mensaje.upper()

		#disminuye
		queueVacio.acquire()
		mutex.acquire()

		x.append(mensaje.split(":"))

		#aumenta
		mutex.release()
		queueLleno.release()


#consumer, segundo thread; quien extrae los "jobs" del queue y los ejecuta
def consumer():
	#para forzarla a que se mantenga global
	global N
	cantidades = {}

	while N > 0:
		queueLleno.acquire()
		mutex.acquire()

		msj = x.pop(0)

		#print(msj)

		mutex.release()
		queueVacio.release()

		N = N - 1
		
		mobileID = msj[0]
		job = int(msj[1])
		if mobileID in cantidades:
			cantidades[mobileID] = cantidades[mobileID] + job
		else:
			cantidades[mobileID] = job

		time.sleep(job)

	for key in cantidades:
		print("Mobile %s consumed %s seconds of CPU" % (key, cantidades[key]))

	return

#creando los threads
threads = []
t1 = threading.Thread(target = consumer)
t2 = threading.Thread(target = producer)

threads.append(t1)
threads.append(t2)


t1.start()
t2.start()

t1.join()
t2.join()

sockete.close()




