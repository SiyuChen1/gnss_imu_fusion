// subber.js
var zmq = require("zeromq"),
  sock = zmq.socket("sub");

sock.connect("tcp://127.0.0.1:5555");
sock.subscribe("kitty cats");
console.log("Subscriber connected to port 5555");

sock.on("message", function(topic, message) {
  console.log(
    "received a message related to:",
    topic,
    "containing message:",
    message
  );
});