from flask import Flask, request, jsonify, session

app = Flask(__name__) #instance of flask

users={'userName':'naomi','password':'admin'}
tasks={
       1:{'taskName':'clean','status':'complete'}
    }

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

    taskName=data.get('taskName')
    status=data.get('status')

    new_task_id=max(tasks.keys()) + 1 if tasks else 1
    tasks[new_task_id] = {'taskName':taskName, 'status':status}
    return jsonify({'message': f'Task {new_task_id} added successfully',"status":201, "data":tasks})

#get tasks
@app.route('/app/v1/get_tasks/',methods=['GET'])
def get_task():
    return jsonify(tasks)

#update task status
@app.route('/app/v1/update_task/<int:taskId>',methods=['PUT'])
def update_task(taskId):
    data=request.get_json()

    if taskId not in tasks:
        return jsonify({"error":"task not found"}) , 404
    
    tasks[taskId]['taskName'] = data['taskName']
    tasks[taskId]['status'] = data['status']

    return jsonify({"message":f"Task {taskId} updated successfully", "status":200,"data":tasks})
    
#delete tasks
@app.route('/app/v1/delete_task/<int:taskId>',methods=['DELETE'])
def delete_task(taskId):
    if taskId in tasks:
        tasks.pop(taskId)
        return jsonify({"message":f"Task {taskId} deleted successfully", "status":200,"data":tasks})
    else:
        return jsonify({"error":"task not found"}) , 404





    




