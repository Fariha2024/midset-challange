from flask import Flask, request, jsonify
from data_analysis import charts, tables, trends, data_processing

app = Flask(__name__)

@app.route('/api/chart/line', methods=['POST'])
def line_chart():
    data = request.get_json()
    image = charts.generate_line_chart(data['data'], data['x_col'], data['y_col'])
    if image:
        return jsonify({'image': image})
    else:
        return jsonify({'error': 'Failed to generate chart'}), 500

@app.route('/api/chart/bar', methods=['POST'])
def bar_chart():
    data = request.get_json()
    image = charts.generate_bar_chart(data['data'], data['x_col'], data['y_col'])
    if image:
        return jsonify({'image': image})
    else:
        return jsonify({'error': 'Failed to generate chart'}), 500

@app.route('/api/chart/pie', methods=['POST'])
def pie_chart():
    data = request.get_json()
    image = charts.generate_pie_chart(data['data'], data['labels'], data['values'])
    if image:
        return jsonify({'image': image})
    else:
        return jsonify({'error': 'Failed to generate chart'}), 500

@app.route('/api/table/data', methods=['POST'])
def data_table():
    data = request.get_json()
    table_data = tables.generate_data_table(data['data'])
    return jsonify({'table': table_data})

@app.route('/api/table/pivot', methods=['POST'])
def pivot_table():
    data = request.get_json()
    pivot_data = tables.generate_pivot_table(data['data'], data['index'], data['columns'], data['values'])
    return jsonify({'pivot': pivot_data})

@app.route('/api/trend/linear', methods=['POST'])
def linear_trend():
    data = request.get_json()
    trend_data = trends.linear_regression(data['data'], data['x_col'], data['y_col'])
    return jsonify({'trend': trend_data})

@app.route('/api/data/clean', methods=['POST'])
def clean_data_route():
    data = request.get_json()
    cleaned_data = data_processing.clean_data(data['data'])
    return jsonify({'cleaned_data': cleaned_data})

if __name__ == '__main__':
    app.run(debug=True)