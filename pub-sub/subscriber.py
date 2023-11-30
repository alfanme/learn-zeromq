import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://127.0.0.1:7000")
socket.setsockopt(zmq.SUBSCRIBE, b"")

while True:
    message = socket.recv_string()
    print("Received message: %s" % message)
