from flask import flask,jsonify,request
app=flask(__name__)
tasks=[
    {
        "data":[
            {
                "contact":"Papa",
                "Phone Number":"8455832090",
                "done":false,
                id:1
            },
            {
                "contact":"Asha",
                "Phone Number":"7077277785",
                "done":false,
                id:2
            },
              {
                "contact":"Arfa Madam",
                "Phone Number":"88888888888",
                "done":false,
                id:1
            }
            
        ]
    }
]
@app.route("/")
def hello_world():
    return "Contact List!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)