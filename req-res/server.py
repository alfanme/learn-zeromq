import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:7000")

while True:
    obj = socket.recv_pyobj()
    print(f"Received message: [ {obj['message']}, {obj['request_number']} ]")

    time.sleep(1)

    #  Send reply back to client
    socket.send_pyobj({"message": "World", "response_number": obj["request_number"]})
