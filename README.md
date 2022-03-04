# numpy-socket
## About
A wrapper for sending numpy array through a socket.

Code framework is based on [ekbanasolutions/numpy-using-socket](https://github.com/ekbanasolutions/numpy-using-socket). 
With some simplification, bug fix and a module seperation between the server and the client.

## Usage
In two different terminals,
```
python test_recver.py --host localhost --port 8090
```
```
python test_sender.py --ip localhost --port 8090
```
If you are using two separate devices, change --host and --ip accordingly, e.g., `--host 0.0.0.0` and `--ip 12.34.0.123`

The code should be running properly on linux desktops and Raspberry Pis (32 bit and 64 bit os). Modify the code as you wish.
