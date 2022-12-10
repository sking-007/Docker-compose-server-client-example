# Import socket module
import socket
import ast


def convertAndDisplay(str):
    data = ast.literal_eval(str)
    for l in data:
        print('- ' + l)


def Main():
    # local host IP '127.0.0.1'
    host = '0.0.0.0'

    # Define the port on which you want to connect
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host, port))

    while True:
        data = s.recv(1024)

        moduleId = input(str(data.decode('ascii')))
        s.send(moduleId.encode('ascii'))

        data = s.recv(1024)

        choice = input(str(data.decode('ascii')))
        s.send(choice.encode('ascii'))

        if (choice == 'L'):
            data = s.recv(1024)
            data = str(data.decode('ascii'))
            if (data != 'Invalid Input'):
                convertAndDisplay(data)
                data = '(A)dd, (E)dit, (D)elete or (R)eturn? ==>> '
                choice = input(data)
                s.send(choice.encode('ascii'))

                if ((choice == 'A') or (choice == 'D')):
                    data = s.recv(1024)
                    choice = input(str(data.decode('ascii')))
                    s.send(choice.encode('ascii'))

                    print('Updated list is')

                    data = s.recv(1024)
                    data = str(data.decode('ascii'))
                    convertAndDisplay(data)

                elif (choice == 'E'):
                    data = s.recv(1024)
                    choice = input(str(data.decode('ascii')))
                    s.send(choice.encode('ascii'))

                    data = s.recv(1024)
                    choice = input(str(data.decode('ascii')))
                    s.send(choice.encode('ascii'))

                    print('Updated list is')

                    data = s.recv(1024)
                    data = str(data.decode('ascii'))
                    convertAndDisplay(data)

                elif (choice == 'R'):
                    pass

        elif (choice == 'C'):
            data = s.recv(1024)
            data = str(data.decode('ascii'))
            print(data)

        elif (choice == 'A'):
            data = s.recv(1024)
            data = str(data.decode('ascii'))
            convertAndDisplay(data)

        elif (choice == 'X'):
                print('Goodbye')
                break
        # # print the received message
        # # here it would be a reverse of sent message
        # print('Received from the server :',str(data.decode('ascii')))

        # ans = input('\nDo you want to continue(y/n) :')
        # if ans == 'y':
        # 	continue
        # else:
        # 	break

    s.close()


if __name__ == '__main__':
    Main()

