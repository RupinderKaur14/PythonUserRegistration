from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from passlib.hash import bcrypt
import sqlite3

app=Flask(__name__)
CORS(app)


@app.route('/user',methods=['POST'])
def get_user():
    data =request.get_json()
    username = data.get('username')
    password = data.get('password')
    #print(user_exists(username))
    #hashed_password = bcrypt.using(rounds=12).hash(password)

    if user_exists(username) == True:
         print(f"User already exists {username} {password}")
         #return jsonify({'message':'user already exists! '})
         abort(401, "Error message goes here")
    else:
        storeData(username, password)
        response_data = {"status": "OK", "message": "user Register sucessfull"}
    
        return jsonify(response_data)
        #return jsonify({'message':'user Register sucessfully'})
        #abort(400, "Error message goes here")
    

# @app.route('/register',methods=['POST'])
# def register_user():
#     data =request.get_json()
    
#     username = data.get('username')
#     password = data.get('password')

#     hashed_password = bcrypt.using(rounds=12).hash(password)

#     if user_exists(username) == True:
#         print(f"User already exists {username} {password}")
#         #return jsonify({'error': 'user already exists!'})
#         return jsonify({'message':'user already exists! '})
#     else:

#         storeData(username, hashed_password)

#         return jsonify({'message':'user Register sucessfully'})



def storeData(username,password):
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()

    # Create a table
    cursor.execute('CREATE TABLE IF NOT EXISTS Registered_User (id INTEGER PRIMARY KEY, username VARCHAR(100), hashedpassword VARCHAR(100))')

    cursor.execute("INSERT INTO Registered_User (username, hashedpassword) VALUES (?, ?)", (username, password))
    connection.commit()
    #connection.close()

def user_exists(username):
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()
    query = "SELECT * FROM Registered_User WHERE username = ?"
    cursor.execute(query,(username,))
    data = cursor.fetchall()
    print("user:", data)
    connection.close()

    if len(data) ==0:
        return False
    else:
        return True
    

app.run()