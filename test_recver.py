
import argparse
import socketNumpy
import numpy as np
import signal

parser = argparse.ArgumentParser(description='None')
parser.add_argument('--host', type=str, default='localhost')
parser.add_argument('--port', type=int, default=8090)
args = parser.parse_args()

listenAddress = args.host
listenPort = args.port

serverSocket = None
def handler(signal_received, frame):
	# Handle any cleanup here
	print('SIGINT or CTRL-C detected. Closing sockets...')
	print("Closing socket")
	try:
		serverSocket.close()
	except:pass
	print("Exit")
	exit(0)

signal.signal(signal.SIGINT, handler)

while True:
    try:
        serverSocket = socketNumpy.SocketServer(listenAddress, listenPort)
        serverSocket.bind_listen_and_accept()
        try:
            while True:
                print("wait for recv...")
                d = serverSocket.receive_array()


                print(d)


                
                serverSocket.send_numpy_array(np.sum(d)/10000)
        except Exception as e:
            print(type(e), "Exception occurred. Close connection...")
            serverSocket.close()
    except Exception as e:
        print(type(e))
        print(e)
        serverSocket.close()
        exit(0)