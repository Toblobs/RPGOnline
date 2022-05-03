### RPGOnline
### A Synergy Studios Project

import socket
from packet import Packet

from threading import Thread
from datetime import datetime

class SocketClient:

    """The socket client which provides a base
       for sending and loading data."""

    def __init__(self, host, port):
        
        self.SERVER_HOST = host
        self.SERVER_PORT = port
        self.MY_IP = socket.gethostbyname(socket.gethostname())

        self.st = '%'
        self.format = 'UTF-8'

        self.s = socket.socket()

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
        self.add_log(f'[/] <Client> state changed to {sta}')
        

    def start_client(self):

        """Starts the connection to the host."""

        self.add_log(f'[*] <Client> Obj @ {self} initialised succesfully')
        self.change_state('~setup')

        try:
            self.add_log(f'[*] <Client> attempting connection to {self.SERVER_HOST}{self.SERVER_PORT}')
            self.s.connect((self.SERVER_HOST, self.SERVER_PORT))

        except BaseException as e:
            self.exit_client(e)

        self.add_log(f'[+] Successfully connected to {self.SERVER_HOST}{self.SERVER_PORT}!')


        self.loop()

    def exit_client(self, error = None):

        """Exits the connection to the server, with an optional error."""

        self.add_log(f'[!] <Client> Socket shutdown, opt error: {error}')
        s.close()

    def send(self, packet):

        """Sends a packet of data to the server, as encoded in the specified format."""

        self.s.send(packet.unwrap(self.st).encode(self.format))

    def listen_for_messages(self):

        """Listens for messages from the host/server."""

        while True:

            try:
                msg = self.s.recv(1024).decode(self.format)
                self.add_log(f'[>] Received message {msg} from the server.')

            except BaseException as e:

                self.exit_client(e)
                break


    def loop(self):

        """The main loop for the client."""

        self.change_state('~running')

        t = Thread(target = self.listen_for_messages)
        t.daemon = True
        t.start()

        while True:

            if self.state == '~running':
                pass

test_userid = 'Toblobs#1234'
test_sessionid = 'ewhfe_jefefe!'

s = SocketClient('127.0.0.1', 4545)
s.start_client()
