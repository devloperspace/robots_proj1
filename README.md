# robots_proj1

 Clone the Repository
 Install Dependencies
 Running the Application
 View the Dashboard
 How It Works
Backend
The backend is built using Flask and Flask-SocketIO. It simulates telemetry data for up to 10 robots, including:

Battery: Random integer between 10 and 100.
CPU Usage: Random integer between 0 and 100.
RAM Usage: Random integer between 0 and 100.
Location: Random latitude and longitude values.
Status: A random boolean indicating whether the robot is online or offline.
The backend updates the robot data every 5 seconds in a separate thread, broadcasting the updated data to all connected clients using WebSocket.

Frontend
The frontend is built with HTML, CSS, and JavaScript. It uses:

Leaflet.js for map rendering.
Socket.io for receiving real-time data from the server.
jQuery for handling AJAX requests to fetch initial data and update the UI.
Real-time Updates
The frontend subscribes to WebSocket events from the backend.
When the data changes, the backend sends updates to the frontend via WebSocket.
The list of robots is updated every 5 seconds, along with their positions on the map.
Map Integration
The robot locations are displayed on a map using Leaflet.js.
Each robot's position is marked as a pin on the map, and clicking on the pin displays the robot's ID and location.
File Structure
