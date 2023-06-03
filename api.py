import sqlite3
from flask import Flask, request, jsonify,g
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

def both_chk(user_id,password):
    with sqlite3.connect('postmaster.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE user=? AND password=?",
                       (user_id, password))
        result = cursor.fetchone()
        count = result[0] if result else 0
        return count
def user_chk(user_id):
    with sqlite3.connect('postmaster.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE user=?", (user_id,))
        result = cursor.fetchone()
        count = result[0] if result else 0
        return count

@api.route('/addUser')
class AddUser(Resource):
    def post(self):
        with sqlite3.connect('postmaster.db') as conn:
            data = api.payload
            if data['name']=='' or data['password']=='':
                return "fill all feilds",200
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users WHERE user = ?", (data['name'],))
            result = cursor.fetchone()
            if result[0] > 0:
            # User already exists
                return "User already exists",202
            else:
                # Insert the new user
                cursor.execute("INSERT INTO users (user, password) VALUES (?, ?)",
                       (data['name'], data['password']))
                conn.commit()
                return {'message': 'Data inserted successfully'}, 201

@api.route('/login')
class UserLogin(Resource):   
    def post(self):
        data = api.payload
        user_id = data['name']
        password = data['password']
        both_match=both_chk(user_id,password)
        user_match=user_chk(user_id)
        if both_match==1:
                return {'message' : "login successful" }, 201
        elif user_match==1:
                return "incorrect password",202
        else:
                return "user not found",200
            
if __name__ == '__main__':
    app.run(debug=True)
