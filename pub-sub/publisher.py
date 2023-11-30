import time
import zmq

context = zmq.Context()

socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:7000")

message = 0

while True:
    print(f"Sending message {message} …")
    socket.send_string(f"{message}", message)

    time.sleep(1)
    message += 1
