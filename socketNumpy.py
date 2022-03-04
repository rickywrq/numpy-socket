import socket
import numpy as np
import pickle
import struct


class SocketClient():
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.type = 'client'

    def connect(self):
        self.socket.connect((self.address, self.port))

    def send_numpy_array(self, np_array):
        data = pickle.dumps(np_array)
        # Send message length first
        message_size = struct.pack("i", len(data))
        # Then data
        self.socket.sendall(message_size + data)

    def receive_array(self):
        self.payload_size = struct.calcsize("i")
        self.data = b''
        while len(self.data) < self.payload_size:
            self.data += self.socket.recv(4096)

        packed_msg_size = self.data[:self.payload_size]
        self.data = self.data[self.payload_size:]
        msg_size = struct.unpack("i", packed_msg_size)[0]

        # Retrieve all data based on message size
        while len(self.data) < msg_size:
            self.data += self.socket.recv(4096)

        frame_data = self.data[:msg_size]
        self.data = self.data[msg_size:]

        # Extract frame
        frame = pickle.loads(frame_data)
        return frame
    
    def send_close_notice(self):
        # Send message length first
        message_size = struct.pack("i", 0)
        # Then data
        self.socket.sendall(message_size)

    def close(self):
        self.socket.close()



class SocketServer():
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.type = None  # server or client

    def bind_listen_and_accept(self):
        self.address = self.address
        self.port = self.port
        self.socket.bind((self.address, self.port))
        print('Socket bind complete')
        self.socket.listen(10)
        self.conn, addr = self.socket.accept()
        print('Socket now listening')
        self.payload_size = struct.calcsize("i")
        self.data = b''

    def send_numpy_array(self, np_array):
        data = pickle.dumps(np_array)
        # Send message length first
        message_size = struct.pack("i", len(data))
        # Then data
        self.conn.sendall(message_size + data)

    def receive_array(self):

        while len(self.data) < self.payload_size:
            self.data += self.conn.recv(4096)

        packed_msg_size = self.data[:self.payload_size]
        self.data = self.data[self.payload_size:]
        msg_size = struct.unpack("i", packed_msg_size)[0]

        if msg_size == 0:
            raise("0 len received, close socket")

        # Retrieve all data based on message size
        while len(self.data) < msg_size:
            self.data += self.conn.recv(4096)

        frame_data = self.data[:msg_size]
        self.data = self.data[msg_size:]

        # Extract frame
        frame = pickle.loads(frame_data)
        return frame
    
    def close(self):
        self.conn.close()


