// Initialize Map
var map = L.map('map').setView([27.2046, 77.4977], 6); // Center on India

// Tile Layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Function to add alert
function addAlert(lat, lon, message) {
  L.marker([lat, lon]).addTo(map)
    .bindPopup("<b>⚠ Alert:</b> " + message).openPopup();

  let log = document.getElementById("alertLog");
  let entry = document.createElement("div");
  entry.classList.add("alert", "alert-danger", "p-2", "mb-2");
  entry.innerText = new Date().toLocaleTimeString() + " - " + message;
  log.prepend(entry);
}

// Simulate random intrusions every 5s
setInterval(() => {
  let lat = 27 + (Math.random() - 0.5) * 10;
  let lon = 77 + (Math.random() - 0.5) * 10;
  addAlert(lat, lon, "Intrusion detected at border point!");
}, 5000);
