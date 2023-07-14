// pubber.js
var zmq = require("zeromq"),
  sock = zmq.socket("pub");

sock.bindSync("tcp://127.0.0.1:5555");
console.log("Publisher bound to port 5555");

setInterval(function() {
  console.log("sending a multipart message envelope");
  sock.send(["kitty cats", "meow!"]);
}, 500);
