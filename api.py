from employs import *

@app.route('/employs', methods=['GET'])
def get_employs():
    return jsonify({'employs': employtable.get_all_employs()})

@app.route('/employs/<int:id>', methods=['GET'])
def get_employ_by_id(id):
    return_value = employtable.get_employbyid(id)
    return jsonify(return_value)

@app.route('/employs/empid/<int:empid>', methods=['GET'])
def get_employ_by_empid(empid):
    return_value = employtable.get_employbyempid(empid)
    return jsonify(return_value)

@app.route('/employs/yearofjoining/<int:yearofjoining>', methods=['GET'])
def get_employ_by_yearofjoining(yearofjoining):
    return_value = employtable.get_employbyyearofjoining(yearofjoining)
    return jsonify(return_value)

@app.route('/employs', methods=['POST'])
def add_employ(): 
    request_data = request.get_json() 
    employtable.add_employ(request_data["empid"], request_data["empname"],request_data["yearofjoining"],request_data["gender"],request_data["position"])
    response = Response("employ added", 201, mimetype='application/json')
    return response


@app.route('/employs/<int:id>', methods=['PUT'])
def update_employ(id): 
    request_data = request.get_json()
    employtable.update_employ(id, request_data["empid"], request_data["empname"],request_data["yearofjoining"],request_data["gender"],request_data["position"])
    response = Response("employ Updated", status=200, mimetype='application/json')
    return response

    

@app.route('/employs/<int:id>', methods=['DELETE'])
def remove_employ(id):
    employtable.delete_employ(id)
    response = Response("employ Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)
