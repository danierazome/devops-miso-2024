from flask import Flask, jsonify, request

app = Flask(__name__)

blacklists = []

@app.route('/blacklist', methods=['POST'])
def create_blacklist():
    data = request.get_json()
    
    blacklists.append(data)
    
    return jsonify({'message': 'Blacklist creada correctamente'}), 201

@app.route('/blacklist/<string:email>', methods=['GET'])
def get_blacklist(blacklist_id):
    blacklist = next((item for item in blacklists if item['id'] == blacklist_id), None)
    
    if blacklist is None:
        return jsonify({'message': 'Blacklist no encontrada'}), 404
    
    return jsonify(blacklist), 200

if __name__ == '__main__':
    app.run(debug=True)
