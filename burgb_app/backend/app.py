from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from items_dao import get_all_items, insert_new_item, delete_item
from sql_connection import get_sql_connection
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Get the path to the frontend directory
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend')

@app.route('/')
def index():
    """Serve the main HTML file"""
    try:
        return send_from_directory(FRONTEND_DIR, 'index.html')
    except FileNotFoundError:
        return jsonify({'error': 'Frontend file not found. Make sure index.html exists in the frontend directory.'}), 404

@app.route('/api/items', methods=['GET'])
def get_items():
    try:
        connection = get_sql_connection()
        items = get_all_items(connection)
        return jsonify(items)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/items', methods=['POST'])
def add_item():
    try:
        connection = get_sql_connection()
        data = request.get_json()
        
        # Validate required fields
        if not data or 'item_name' not in data or 'unit_id' not in data or 'price_per_item' not in data:
            return jsonify({'error': 'Missing required fields: item_name, unit_id, price_per_item'}), 400
        
        item_id = insert_new_item(connection, {
            'item_name': data['item_name'],
            'unit_id': data['unit_id'],
            'price_per_item': float(data['price_per_item'])
        })
        
        return jsonify({'message': 'Item added successfully', 'item_id': item_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def remove_item(item_id):
    try:
        connection = get_sql_connection()
        delete_item(connection, item_id)
        return jsonify({'message': 'Item deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/units', methods=['GET'])
def get_units():
    """Get available units for the dropdown"""
    return jsonify([
        {'unit_id': 1, 'unit_name': 'each'},
        {'unit_id': 2, 'unit_name': 'lb'}
    ])

if __name__ == '__main__':
    app.run(debug=True, port=5000)

