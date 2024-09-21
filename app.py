from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
swagger = Swagger(app)

# Määrittele käyttäjämalli
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'age': self.age}

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Get all users
    ---
    responses:
      200:
        description: A list of users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              age:
                type: integer
    """
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The ID of the user to retrieve
    responses:
      200:
        description: A user object
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            age:
              type: integer
      404:
        description: User not found
    """
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/api/users', methods=['POST'])
def add_user():
    """
    Add a new user
    ---
    parameters:
      - name: user
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            age:
              type: integer
    responses:
      201:
        description: User created
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            age:
              type: integer
      400:
        description: Invalid input
    """
    new_user = request.get_json()
    if not new_user.get('name'):
        return jsonify({"message": "Name is required"}), 400
    if not isinstance(new_user.get('age'), int) or new_user['age'] <= 0:
        return jsonify({"message": "Age must be a positive integer"}), 400

    user = User(name=new_user['name'], age=new_user['age'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
      - name: user
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            age:
              type: integer
    responses:
      200:
        description: User updated
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            age:
              type: integer
      400:
        description: Invalid input
      404:
        description: User not found
    """
    user = User.query.get(user_id)
    if user:
        data = request.get_json()
        if not data.get('name'):
            return jsonify({"message": "Name is required"}), 400
        if not isinstance(data.get('age'), int) or data['age'] <= 0:
            return jsonify({"message": "Age must be a positive integer"}), 400

        user.name = data['name']
        user.age = data['age']
        db.session.commit()
        return jsonify(user.to_dict())
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
