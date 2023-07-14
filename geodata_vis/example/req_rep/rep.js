var zmq = require("zeromq"),
    sock = zmq.socket("rep");

sock.bind("tcp://127.0.0.1:8888");
console.log("Subscriber connected to port 8888");

sock.on('message', function(topic) {
    sock.send("I am server, giving you reply")
    msg = Buffer.from(topic, "utf-8").toString().split(",")
    console.log('received first number = ', msg[0], ", second number = ", msg[1]);
});