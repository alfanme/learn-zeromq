import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:7000")

while True:
    message = socket.recv_string()
    print("Received message: %s" % message)

    time.sleep(1)
