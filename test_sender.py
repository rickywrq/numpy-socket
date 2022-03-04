# test_sender

import argparse
import socketNumpy
import numpy as np


parser = argparse.ArgumentParser(description='None')
parser.add_argument('--ip', type=str, default='localhost')
parser.add_argument('--port', type=int, default=8090)
args = parser.parse_args()

serverAddress = args.ip
serverPort = args.port

while True:
    try:
        clientSocket = socketNumpy.SocketClient(serverAddress, serverPort)
        clientSocket.connect()
        break
    except:
        continue

for i in range(100):
    
    
    data = np.ones((100,100))*i
    clientSocket.send_numpy_array(data)
    recv = clientSocket.receive_array()
    print(recv)
clientSocket.send_close_notice()
clientSocket.close()