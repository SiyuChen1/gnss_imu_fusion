document.addEventListener('DOMContentLoaded', () => {
  // Connect to the server via Socket.IO
  const socket = io();
  var index = 0
  // Create a map centered on a default location
  const map = L.map('map').setView([37.7749, -122.4194], 12); // Adjust the zoom level as desired

  // Create a tile layer using OpenStreetMap data
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
    maxZoom: 18
  }).addTo(map);

  // Listen for geodata updates from the server
  socket.on('geodata', (geodata) => {
    // Update the map with the new geodata
    console.log('Received geodata:', geodata);
    msg = geodata.split(",")
    latitude = parseFloat(msg[0])
    longitude = parseFloat(msg[1])
    // Add a marker for the GPS coordinates
    L.marker([latitude, longitude]).addTo(map)
    .bindPopup(`GPS Location ${index}`)
    .openPopup();
    // Add your custom logic here to update the map based on the new geodata
    index = index + 1;
  });
});

  