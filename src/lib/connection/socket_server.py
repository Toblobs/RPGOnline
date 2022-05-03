### RPGOnline
### A Synergy Studios Project

import socket
from packet import Packet

from threading import Thread
from datetime import datetime

class SocketServer:

    """The server, which retrieves commands from the players
       and sends level data to specific clients."""

    def __init__(self, host, port):

        self.SERVER_HOST = host
        self.SERVER_PORT = port
        self.MY_IP = socket.gethostbyname(socket.gethostname())

        self.st = '%'
        self.format = 'UTF-8'
        
        self.s = socket.socket()
        self.max_users = 4

        self.client_sockets = set()
        self.client_addr = {}

        self.buffer = []
        self.buffer_addition = False

        self.log = {}

        self.state = '~init'

    def add_log(self, l):

        """Adds a specific value to the log."""

        time = datetime.now()

        self.log[f'{time.hour}:{time.minute}:{time.second}'] = l

        print(str(list(self.log.keys())[-1]) + ': ' + str(list(self.log.values())[-1]))

    def change_state(self, sta):

        """Changes the state of the server to the selected state, and adds a log."""

        self.state = sta
        self.add_log(f'[/] <Server> state changed to {sta}')

    def start_server(self):

        """Starts the server and server loop thread."""

        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.SERVER_HOST, self.SERVER_PORT))
        self.s.listen(self.max_users)

        self.add_log(f'[*] <Server> Obj @ {self} initialised succesfully')

        self.change_state('~setup')
        
        self.loop()

    def exit_server(self, error = None):

        """Exits the server with an optional error."""

        for cs in self.client_sockets:
            cs.close()

        self.s.close()

        self.add_log(f'[*] <Server> Socket shutdown, opt error: {error}')

    def send(self, cs, packet):

        """Sends data to the client as encoded in the specified format."""

        cs.send(packet.unwrap(self.st).encode(self.format))

        self.add_log(f'[>] <Server> sent <Packet> {packet.comm}/{packet.det} to <Client> {self.client_addr[cs]}')

    def broadcast(self, packet):

        """Broadcasts the data to every client that is connected."""

        for cs in self.client_sockets:
            cs.send(packet.unwrap(self.st).encode(self.format))

    def new_client(self, client_socket, client_address):

        """Adds a new client to the server."""

        self.client_sockets.add(client_socket)
        self.client_add[client_socket] = client_address

        self.add_log(f'[*] <Server> accepted new client: {client_address}')

        t = Thread(target = self.listen_for_client, args = (client_socket,), daemon = True)

        t.start()
        
    def client_disconnected(self, cs, e):

        """Exits a connection with a client."""

        self.add_log(f'[!] <Client> {self.client_addr[cs]} disconnected from <Server>: {e}')

        del self.client_addr[cs]
        cs.close()
        

    def listen_for_client(self, cs):

        """Listens for a client sending commands to the server."""

        while True:

            try:

                msg = cs.recv(1024).decode()
                msg = msg.split(self.st)

                pk = Packet(msg[0], msg[1])

            except BaseException as e:

                self.client_disconnected(cs, e)
                break

            else:

                print(pk)

    def loop(self):

        """Looping the program, adding new clients, checking recieved data
           and logging details."""

        while True:

            if self.state == '~setup':

                # Setup state

                self.change_state('~running')

            if self.state == '~running':

                try:

                    client_socket, client_address = self.s.accept()
                    self.new_client(client_socket, client_address)

                except:

                    pass


        self.exit_server()

                    

s = SocketServer('0.0.0.0', 4545)
s.start_server()
