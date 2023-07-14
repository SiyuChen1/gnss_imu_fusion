import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:8888")

# important !!!
socket.setsockopt_string(zmq.SUBSCRIBE, "")

while True:
    string = socket.recv().decode()
    lat, lon = string.split(",")
    print(lat, lon)