Stephanie M. Ramos Camacho

Instrucciones del proyecto:
En este proyecto tuvimos que simular un algoritmo de programación FIFO para un sistema distribuido que consta de dispositivos móviles y un servidor de cómputo central. Asumimos que teníamos múltiples dispositivos móviles que generaban problemas computacionales que son demasiado pesados para ser ejecutados en su hardware. Simulamos un servidor central de anuncios que recibirá solicitudes de tiempo de cómputo de los dispositivos móviles, colocará los trabajos en una cola de procesos y luego los "ejecutará".

Este programa/problema simula una fila (que son los servidores) y dirá cuánto tiempo se tardó en terminar su trabajo. Este es el problema, hay móviles (pueden ser muchos a la vez) enviando al servidor de una computadora el mensaje que desean desplegar y se toman un tiempo de "sleep". La computadora los recibe y empieza a escribir cuánto tiempo se ha enviado por cada móvil para estar en el CPU. Se "duerme" esa cantidad de tiempoy cuando reciba una cantidad total de mensajes, entonces envía cuánto tiempo envió cada móvil. Se crean dos threads; uno que es el "producer" (que sería el móvil) que presta atención al mensaje y pone los "jobs" en el queue y el otro que es el "consumer", quien extrae los "jobs" del queue y los ejecuta. El "producer" toma el tiempo y el ID y los guarda en el queue y el "consumer" coge el mensaje del queue, guarda la suma total del tiempo acumulado en el queue por cada "job" y el tiempo de "sleep" extraido del queue.

mobile.py
Estos programas deben recibir como parámetros la identificación móvil, la dirección del servidor y el puerto del servidor. Genera un tiempo de simulación aleatorio que se enviará como mensaje al servidor de cómputo con la identificación de móvil.

scheduler.py
Estos programas deben recibir como parámetro el puerto del servidor. Este programa tendrá dos hilos(threads). El primero se encargará de recibir los mensajes enviados desde mobile.py y ponerlos en queue. El segundo eliminará el mensaje del queue, actualizará el tiempo de simulación total de cada dispositivo móvil y suspenderá el tiempo de simulación por instrucción que simule la ejecución del proceso. Al final, el programa imprimirá el tiempo de simulación total de cada móvil.

Para ejecutar el programa, tenemos que decidir la cantidad límite de mensajes que queremos recibir (cambiando el valor de la variable n en scheduler.py) y luego ejecutar el siguiente comando:
python scheduler.py <server port>
después abres otro "tab" del terminal con el comando:
python mobile.py <mobile ID> <server address> <server port>
dependiendo de cuántos móviles queramos ejecutar al mismo tiempo.

El puerto del servidor debe ser el mismo en ambos comandos.
El progrma se usa desde el terminal y se pone algo como scheduler.py 4096, luego crea los móviles con su ID y el servidor que se estén usando con el server port (localhost); algo como mobile.py 2 localhost 4096.

Personas que me ayudaron con este proyecto:
Carlos Díaz
María Ramos
Oniel