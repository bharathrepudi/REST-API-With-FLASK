from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (dictionary)
users = {}

# Home route
@app.route('/')
def home():
    return "Welcome to the User Management API!"

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET user by ID
@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user}), 200
    return jsonify({"error": "User not found"}), 404

# POST - Create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = data.get('id')
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400
    users[user_id] = {
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify({"message": "User created"}), 201

# PUT - Update user
@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])
    return jsonify({"message": "User updated"}), 200

# DELETE - Remove user
@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

# Run app
if __name__ == '__main__':
    app.run(debug=True)
