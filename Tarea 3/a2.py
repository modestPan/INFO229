#!/usr/bin/env python
import pika, sys, os
import wikipedia

def main():

    #Conexión al servidor RabbitMQ   
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    #Nos aseguramos que existe una cola 'hello'
    channel.queue_declare(queue='wiki')


    #Recibir mensajes de la cola es más complejo. Funciona suscribiendo una función de devolución de llamada
    #  ("callback"). Cada vez que recibimos un mensaje, esta función "callback" es llamada por la libreria Pika.
    #  En nuestro caso, esta función imprimirá en la pantalla el contenido del mensaje.
    rs = None
    
    def callback(ch, method, properties, body):
        txt = ""
        for i in body:
            txt = txt + chr(i) 
            
        print(" [x] Received ", txt )
        search = wikipedia.page(txt)
        resumme = wikipedia.summary(txt, sentences = 3)
        print(' > url: %r' % search)
        print(' > summary: %r' % resumme)
    channel.basic_consume(queue='wiki', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()





    #Bocle infinita
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)