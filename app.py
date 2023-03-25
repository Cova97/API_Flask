from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('data.json', 'r') as file:
    data = json.load(file)

# Ruta para obtener todos los registros
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# Ruta para obtener un registro específico
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    new_item = []
    for item in data:
        if item['id'] == item_id:
            new_item.append(item)
    item = new_item
    return jsonify(item)

# Ruta para crear un nuevo registro
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = len(data) + 1
    new_item['status'] = False
    data.append(new_item)
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    return jsonify(new_item)

# Ruta para actualizar un registro existente
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.get_json()
    for item in data:
        if item['id'] == item_id:
            #data[i] = updated_item
            item['status'] = True
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    return jsonify(updated_item)

# Ruta para eliminar un registro existente
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    new_item = []
    for item in data:
        if item['id'] == item_id:
            new_item.append(item)
    item = new_item
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__':
    app.run(debug = True)

# Comentario para un deploy