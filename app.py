from flask import Flask, request, jsonify, session

app = Flask(__name__) #instance of flask

users={'userName':'naomi','password':'admin'}


#ROUTES
#register user
@app.route('/app/v1/register/',methods=['POST'])
def register():
    data=request.get_json()
    #retrieves JSON data from request body

    #extract values and assigns it
    userName=data.get('userName')
    password=data.get('password')

    #add new user
    new_user={'userName':userName,'password':password}
    users.update(new_user)
    return {"message":"User successfully authenticated", "status":201, "data":users}
