import flask
import datetime
from flask import request, jsonify
from mockData import employees, leaveBalances, leave, pays, roster

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Shay's App Testing API</h1> <p>This API is used for creating and testing web and mobile applications</p>"

@app.route('/api/uscorr/auth/employee', methods=['GET'])
def getEmployees():
    
    # id should be a valid employee number
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field was provided.  Specify an id field containing a valid employee number"

    results = []

    for employee in employees:
        if employee['employeeNumber'] == id:
            results.append(employee)

    if len(results) < 1:
        return "No match for found for the specified employee number"
    else:
        return jsonify(results)

@app.route('/api/uscorr/sap/balances/<employeeNo>', methods=['GET'])
def getLeaveBalances(employeeNo):

    # id should be a valid employee number
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field was provided.  Specify an id field containing a valid employee number"

    results = []

    for balance in leaveBalances:
        if balance['employeeNumber'] == id:
            results.append(balance)

    if len(results) < 1:
        return "No match for found for the specified employee number"
    else:
        return jsonify(results)

@app.route('/api/uscorr/sap/pay/<employeeNo>', methods=['GET'])
def getPays(employeeNumber):
    # id should be a valid employee number
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field was provided.  Specify an id field containing a valid employee number"

    results = []

    for pay in pays:
        if pay['employeeNumber'] == id:
            results.append(pay)

    if len(results) < 1:
        return "No match for found for the specified employee number"
    else:
        return jsonify(results)

@app.route('/api/uscorr/sap/leave/<employeeNo>', methods=['GET'])
def getLeave(employeeNo):
    # id should be a valid employee number
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field was provided.  Specify an id field containing a valid employee number"

    results = []

    for app in leave:
        if app['employeeNumber'] == id:
            results.append(app)

    if len(results) < 1:
        return "No match for found for the specified employee number"
    else:
        return jsonify(results)

@app.route('/api/uscorr/roster/<employeeNo>', methods=['GET'])
def getRoster(employeeNo):
    # id should be a valid employee number
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field was provided.  Specify an id field containing a valid employee number"

    results = []

    for shift in roster:
        if shift['employeeNumber'] == id:
            results.append(shift)

    if len(results) < 1:
        return "No match for found for the specified employee number"
    else:
        return jsonify(results)

app.run()
