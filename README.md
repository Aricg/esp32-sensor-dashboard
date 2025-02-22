# ESP32 Sensor Dashboard

A Python-based web server for displaying sensor data from ESP32 devices.

## Features

- Accepts POST requests with sensor data
- Dynamically generates and updates graphs for each sensor
- Real-time visualization of sensor readings

## Setup

1. Install dependencies:
   ```bash
   pip install -r web_server/requirements.txt
   ```
2. Run the server:
   ```bash
   python web_server/app.py
   ```
3. Access the dashboard at `http://localhost:5050`

## Accessing the Server on Your LAN

1. Find your Mac's LAN IP address:
   ```bash
   ifconfig | grep "inet "
   ```
2. Access the dashboard from another device on the same network:
   ```
   http://<your-lan-ip>:5050
   ```
3. Post data to the server:
   ```bash
   curl -X POST -H "Content-Type: application/json" \
        -d '{"service_name": "test_service", "sensor_name": "temp_sensor", "sensor_value": 25.5}' \
        http://<your-lan-ip>:5050/data
   ```

## Posting Data

Use `curl` or any HTTP client to send POST requests:

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"service_name": "test_service", "sensor_name": "temp_sensor", "sensor_value": 25.5}' \
     http://localhost:5050/data
```

## Deployment

### With Gunicorn

```bash
gunicorn -w 4 web_server.app:app
```

### With Docker

1. Build the Docker image:
   ```bash
   docker build -t esp32-dashboard .
   ```
2. Run the container:
   ```bash
   docker run -p 5050:5050 esp32-dashboard
   ```

## License

MIT License. See [LICENSE](LICENSE) for details.
