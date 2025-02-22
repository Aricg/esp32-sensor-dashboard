from flask import Flask, request, jsonify, render_template
import plotly
import plotly.graph_objs as go
import json
from collections import defaultdict

app = Flask(__name__)

# In-memory storage for sensor data
sensor_data = defaultdict(list)

@app.route('/', methods=['GET'])
def index():
    # Generate graphs for all sensors
    graphs = []
    for sensor_name, values in sensor_data.items():
        graph = go.Scatter(
            x=list(range(len(values))),
            y=values,
            mode='lines+markers',
            name=sensor_name
        )
        layout = go.Layout(title=f'Sensor: {sensor_name}', xaxis_title='Time', yaxis_title='Value')
        graphs.append(json.dumps({'data': [graph], 'layout': layout}, cls=plotly.utils.PlotlyJSONEncoder))
    return render_template('index.html', graphs=graphs)

@app.route('/data', methods=['POST'])
def receive_data():
    # Parse incoming JSON data
    data = request.json
    if not data or 'service_name' not in data or 'sensor_name' not in data or 'sensor_value' not in data:
        return jsonify({'error': 'Missing or invalid fields'}), 400

    # Store sensor data
    sensor_name = data['sensor_name']
    sensor_value = float(data['sensor_value'])
    sensor_data[sensor_name].append(sensor_value)

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
