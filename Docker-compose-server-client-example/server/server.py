import socket

from _thread import *
import threading
import dataStructures
import time
import pika


def listToString(s):
    str = " "
    return (str.join(s))

# thread function


def threaded(c, ip):

    # Connecting to the RabbitMQ Service
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='logs')
    channel.basic_publish(exchange='', routing_key='logs',
                          body='Connected to Server')

    while True:
        message = 'What is the module id? ==>> '
        c.send(message.encode('ascii'))

        moduleId = c.recv(1024)
        moduleId = str(moduleId.decode('ascii'))

        message = '(L)earning Outcomes, (C)ourses, (A)ssessments or e(X)it? ==>> '
        c.send(message.encode('ascii'))
        choice = c.recv(1024)
        choice = str(choice.decode('ascii'))

        if (choice == 'L'):
            outcomes = dataStructures.learningOutcomes[moduleId]
            message = str(outcomes)
            c.send(message.encode('ascii'))

            change = c.recv(1024)
            change = str(change.decode('ascii'))

            if (change == 'A'):
                # Sending signal to RabbitMQ
                body = moduleId+' Learning Outcome Added'+' '+ip
                channel.basic_publish(
                    exchange='', routing_key='logs', body=body)

                message = 'Enter new LO description ==>> '
                c.send(message.encode('ascii'))

                newLo = c.recv(1024)
                newLo = str(newLo.decode('ascii'))

                dataStructures.learningOutcomes[moduleId].append(newLo)

                outcomes = dataStructures.learningOutcomes[moduleId]
                message = str(outcomes)
                c.send(message.encode('ascii'))
                time.sleep(1)

            elif (change == 'D'):

                # Sending signal to RabbitMQ
                body = moduleId+' Learning Outcome Deleted'+' '+ip
                channel.basic_publish(
                    exchange='', routing_key='logs', body=body)

                message = 'Enter LO # ==>> '
                c.send(message.encode('ascii'))

                newLo = c.recv(1024)
                newLo = str(newLo.decode('ascii'))

                dataStructures.learningOutcomes[moduleId].pop(int(newLo))

                outcomes = dataStructures.learningOutcomes[moduleId]
                print('Printing outcomes',outcomes)
                message = str(outcomes)
                c.send(message.encode('ascii'))
                time.sleep(1)


            elif (change == 'E'):

                # Sending signal to RabbitMQ
                body = moduleId+' Learning Outcome Added'+' '+ip
                channel.basic_publish(
                    exchange='', routing_key='logs', body=body)

                message = 'Enter LO # ==>> '
                c.send(message.encode('ascii'))

                newLoNum = c.recv(1024)
                newLoNum = str(newLoNum.decode('ascii'))

                message = 'Enter new LO # ==>> '
                c.send(message.encode('ascii'))

                newLo = c.recv(1024)
                newLo = str(newLo.decode('ascii'))

                dataStructures.learningOutcomes[moduleId][int(
                    newLoNum)] = newLo

                outcomes = dataStructures.learningOutcomes[moduleId]
                message = str(outcomes)
                c.send(message.encode('ascii'))
                time.sleep(1)

                

            elif (change == 'E'):
                pass

        elif (choice == 'C'):
            message = dataStructures.course
            c.send(message.encode('ascii'))
            time.sleep(1)

        elif (choice == 'A'):
            outcomes = dataStructures.assessments
            message = str(outcomes)
            c.send(message.encode('ascii'))
            time.sleep(1)

        elif (choice == 'X'):
            break
        else:
            print('Invalid Input')

    print('Bye')
    c.close()


def Main():
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        ip = str(addr[0]) + ':' + str(addr[1])
        print(ip)
        start_new_thread(threaded, (c, ip))
    s.close()
    connection.close()


if __name__ == '__main__':
    Main()
