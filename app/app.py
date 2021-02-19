import flask
import datetime
from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

employees = [
    { 
        'employeeNumber': 123456,
        'firstName': 'Joe',
        'lastName': 'Bloggs',
        'userName': 'bloggjo',
        'displayName': 'BLOGGS, Joe (User)'
    },
    { 
        'employeeNumber': 432156,
        'firstName': 'Jane',
        'lastName': 'Doe',
        'userName': 'doeja',
        'displayName': 'DOE, Jane (User)'
    },
    { 
        'employeeNumber': 7654674,
        'firstName': 'Peter',
        'lastName': 'Graham',
        'userName': 'grahpe',
        'displayName': 'GRAHAM, Peter (User)'
    }
]

leaveBalances = [
    {
        'employeeNumber': 123456,
        'annual': 420,
        'lieu': 42,
        'sick': 10
    },
    {
        'employeeNumber': 432156,
        'annual': 100,
        'lieu': 8,
        'sick': 25
    },
    {
        'employeeNumber': 7654674,
        'annual': -40,
        'lieu': 0,
        'sick': 0
    }
]

pays = [
    {
        'employeeNumber': 123456,
        'date': datetime.datetime(2021,2,3),
        'amount': 2352.95,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 123456,
        'date': datetime.datetime(2021,2,17),
        'amount': 2352.95,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 123456,
        'date': datetime.datetime(2021,3,3),
        'amount': 2352.95,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 123456,
        'date': datetime.datetime(2021,3,17),
        'amount': 2352.95,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 123456,
        'date': datetime.datetime(2021,3,31),
        'amount': 2352.95,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 432156,
        'date': datetime.datetime(2021,2,3),
        'amount': 1734.50,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 432156,
        'date': datetime.datetime(2021,2,17),
        'amount': 1734.50,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 432156,
        'date': datetime.datetime(2021,3,3),
        'amount': 1734.50,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 432156,
        'date': datetime.datetime(2021,3,17),
        'amount': 1734.50,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 432156,
        'date': datetime.datetime(2021,3,31),
        'amount': 1734.50,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 7654674,
        'date': datetime.datetime(2021,2,3),
        'amount': 3215.42,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 7654674,
        'date': datetime.datetime(2021,2,17),
        'amount': 3215.42,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 7654674,
        'date': datetime.datetime(2021,3,3),
        'amount': 3215.42,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 7654674,
        'date': datetime.datetime(2021,3,17),
        'amount': 3215.42,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
    {
        'employeeNumber': 7654674,
        'date': datetime.datetime(2021,3,31),
        'amount': 3215.42,
        'payslipURL': 'https://www.smartsheet.com/sites/default/files/IC-Printable-Pay-Stub-Template-Updated-8903-PDF.pdf'
    },
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Shay's App Testing API</h1> <p>This API is used for creating and testing web and mobile applications</p>"

@app.route('/api/uscorr/auth/employee', methods=['GET'])
def getEmployees():
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
    return jsonify(leaveBalances)

@app.route('/api/uscorr/sap/pay/<employeeNo>', methods=['GET'])
def getPays(employeeNumber):
    return jsonify(pays)

@app.route('/api/uscorr/sap/leave/<employeeNo>', methods=['GET'])
def getLeave(employeeNo):
    return "Todo"

@app.route('/api/uscorr/roster/<employeeNo>', methods=['GET'])
def getRoster(employeeNo):
    return "Todo"

app.run()
