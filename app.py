from flask import Flask, request, jsonify, session

app = Flask(__name__) #instance of flask

users={'userName':'naomi','password':'admin'}
tasks={'taskId':1,'taskName':'clean','status':'complete'}

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

#login user
@app.route('/app/v1/login/',methods=['POST'])
def login():
    data=request.get_json()
    password=data.get('password')
    if "userName" in users and password==users.get("password"):
        return {"message":"User successfully authenticated", "status":200}
        
    else:
        return None

#get users
@app.route('/app/v1/users/',methods=['GET'])
def get_user():
    return jsonify(users)

#create tasks
@app.route('/app/v1/create_tasks/',methods=['POST'])
def create_task():
    data=request.get_json()

    taskId=data.get('taskId')
    taskName=data.get('taskName')
    status=data.get('status')

    new_task={'taskId':taskId,'taskName':taskName,'status':status}
    tasks.update(new_task)
    return {"message":"Task successfully added", "status":201, "data":tasks}

#get tasks
@app.route('/app/v1/get_tasks/',methods=['GET'])
def get_task():
    return jsonify(tasks)
