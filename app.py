from flask import Flask, request, jsonify, session

app = Flask(__name__) #instance of flask

users={'userName':'naomi','password':'admin'}
tasks={
        'taskId':1,
        'taskName':'clean',
        'status':'complete'
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

#update task status
@app.route('/app/v1/update_task/<int:taskId>',methods=['PUT'])
def update_task(taskId):
    data=request.get_json()
    taskId=tasks.get('taskId')
    
    if "taskId" in tasks and taskId==tasks.get("taskId"):
        taskName=data.get('taskName')
        status=data.get('status')

    
        updated_task={'taskId':taskId,'taskName':taskName,'status':status}
        tasks.update(updated_task)

        return {"message":"Task updated successfully", "status":200,"data":updated_task}

#delete tasks
@app.route('/app/v1/delete_task/<int:taskId>',methods=['DELETE'])
def delete_task(taskId):
    data=request.get_json()
    taskId=tasks.get('taskId')
    if taskId not in tasks:
        return jsonify({"error":"user not found"}) , 404
    
    del tasks[taskId]
    return jsonify({"message":"User Deleted Successfully"}), 200





    




