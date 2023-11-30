import time
import zmq

context = zmq.Context()

socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:7000")

message = 0

while True:
    print(f"Sending message {message} …")
    socket.send_string(f"{message}")

    time.sleep(1 / 3)
    message += 1
