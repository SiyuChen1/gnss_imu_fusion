const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);
const zmq = require('zeromq');

// Serve static files from the "public" directory
app.use(express.static('public'));

// Start the server
const port = 3000;
server.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

// Configure ZeroMQ subscriber
const zmqPort = 8888;

zmqSub = zmq.socket("sub");
zmqSub.connect(`tcp://127.0.0.1:${zmqPort}`);
zmqSub.subscribe('');
console.log(`ZeroMQ Sub is listening on port ${zmqPort}`);

// Configure Socket.IO
io.on('connection', (socket) => {
  console.log('Client connected');

  // Receive geodata from ZeroMQ publisher
  zmqSub.on("message", function(message) {
    msg = Buffer.from(message, "utf-8").toString()
    console.log(msg);
    socket.emit('geodata', msg);
  });

  // Disconnect event
  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});
