import zmq
import numpy as np
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:8888")

latitude = 37.7749
longitude = -122.4194

index = 1

while True:
    # lat = latitude + 1e-3 * np.random.randn()
    # lon = longitude + 1e-3 * np.random.randn()
    lat = latitude + 1e-4 * index
    lon = longitude + 1e-4 * index
    req = "{}, {}".format(lat, lon)
    socket.send(req.encode())
    print(req)
    index += 1
    time.sleep(1)