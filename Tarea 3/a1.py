#!/usr/bin/env python
import pika

# iniciar docker sudo /etc/init.d/docker start


#Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Creación de la cola
channel.queue_declare(queue='wiki')
vs = "Argentina"

#Publicación del mensaje
channel.basic_publish(exchange='',
                      routing_key='wiki',
                      body=vs)

print(" [+] The message is: ", vs)

connection.close()