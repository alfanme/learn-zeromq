import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:7000")

request_number = 0

while True:
    print("Sending request %s …" % request_number)
    socket.send_pyobj({"message": "Hello", "request_number": request_number})

    #  Get the reply
    obj = socket.recv_pyobj()
    print(f"Received reply [ {obj['message']}, {obj['response_number']} ]")

    request_number += 1
