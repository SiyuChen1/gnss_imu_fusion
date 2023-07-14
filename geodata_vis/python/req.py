import zmq
import numpy as np
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:8888")

latitude = 37.7749
longitude = -122.4194

while True:
    lat = latitude + 1e-3 * np.random.randn()
    lon = longitude + 1e-3 * np.random.randn()
    req = "{}, {}".format(lat, lon)
    print(req)
    socket.send(req.encode())
    # Receive the response from the server
    response = socket.recv()
    print("Received response:", response.decode())
    time.sleep(1)
    