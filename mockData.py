import datetime

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

leave = [
  {
    "employeeNumber": 432156,
    "leaveType": "Sick",
    "status": "Pending",
    "date": "04/05/17",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Berevement",
    "status": "Approved",
    "date": "25/07/18",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Berevement",
    "status": "Declined",
    "date": "15/11/17",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Sick",
    "status": "Declined",
    "date": "27/09/18",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Other",
    "status": "Pending",
    "date": "21/06/18",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Annual",
    "status": "Declined",
    "date": "27/12/17",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Lieu",
    "status": "Declined",
    "date": "23/02/18",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "ACC",
    "status": "Declined",
    "date": "17/07/20",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Berevement",
    "status": "Pending",
    "date": "09/09/19",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "ACC",
    "status": "Approved",
    "date": "12/01/19",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Annual",
    "status": "Declined",
    "date": "12/07/19",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Sick",
    "status": "Pending",
    "date": "19/09/20",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Sick",
    "status": "Declined",
    "date": "06/05/17",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Other",
    "status": "Approved",
    "date": "10/10/19",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Other",
    "status": "Declined",
    "date": "29/11/20",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Unpaid",
    "status": "Declined",
    "date": "24/07/19",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Berevement",
    "status": "Declined",
    "date": "11/11/18",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Sick",
    "status": "Withdrawn",
    "date": "24/12/17",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Berevement",
    "status": "Pending",
    "date": "12/03/20",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Unpaid",
    "status": "Approved",
    "date": "01/12/17",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Berevement",
    "status": "Declined",
    "date": "17/08/17",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Annual",
    "status": "Pending",
    "date": "01/03/18",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Other",
    "status": "Pending",
    "date": "03/12/18",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Berevement",
    "status": "Approved",
    "date": "19/02/19",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Sick",
    "status": "Approved",
    "date": "14/08/18",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Other",
    "status": "Withdrawn",
    "date": "12/04/17",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Sick",
    "status": "Declined",
    "date": "20/06/20",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Domestic",
    "status": "Pending",
    "date": "05/04/17",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Lieu",
    "status": "Declined",
    "date": "07/04/19",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Special",
    "status": "Pending",
    "date": "14/01/20",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "ACC",
    "status": "Withdrawn",
    "date": "08/04/19",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Annual",
    "status": "Declined",
    "date": "03/05/18",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Domestic",
    "status": "Withdrawn",
    "date": "12/05/17",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Domestic",
    "status": "Declined",
    "date": "13/12/19",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Domestic",
    "status": "Approved",
    "date": "25/08/19",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Special",
    "status": "Approved",
    "date": "01/03/20",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "ACC",
    "status": "Declined",
    "date": "20/09/20",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Unpaid",
    "status": "Approved",
    "date": "23/05/17",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Special",
    "status": "Approved",
    "date": "22/07/17",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Special",
    "status": "Declined",
    "date": "12/04/17",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Special",
    "status": "Withdrawn",
    "date": "14/03/17",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Unpaid",
    "status": "Approved",
    "date": "18/10/18",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Sick",
    "status": "Declined",
    "date": "26/07/19",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Special",
    "status": "Declined",
    "date": "14/04/20",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "ACC",
    "status": "Declined",
    "date": "06/07/18",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "ACC",
    "status": "Pending",
    "date": "06/03/20",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Lieu",
    "status": "Approved",
    "date": "14/09/20",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "ACC",
    "status": "Pending",
    "date": "02/09/20",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Annual",
    "status": "Pending",
    "date": "24/05/19",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Domestic",
    "status": "Approved",
    "date": "10/06/18",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "ACC",
    "status": "Pending",
    "date": "15/03/20",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Berevement",
    "status": "Pending",
    "date": "11/05/17",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Special",
    "status": "Declined",
    "date": "12/12/20",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Sick",
    "status": "Pending",
    "date": "09/11/20",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Domestic",
    "status": "Approved",
    "date": "10/07/17",
    "comments": ""
  },
  {
    "employeeNumber": 432156,
    "leaveType": "Special",
    "status": "Withdrawn",
    "date": "14/11/18",
    "comments": ""
  },
  {
    "employeeNumber": 7654674,
    "leaveType": "Lieu",
    "status": "Approved",
    "date": "10/12/20",
    "comments": ""
  },
  {
    "employeeNumber": 123456,
    "leaveType": "Berevement",
    "status": "Declined",
    "date": "15/12/17",
    "comments": ""
  }
]

roster = [
  {
    "employeeNumber": 432156,
    "status": "RDO",
    "date": "13/06/18",
    "label": "1800-0600 RO-CO"
  },
  {
    "employeeNumber": 7654674,
    "status": "Leave",
    "date": "06/02/18",
    "label": "0600-1800 TRAN-CO"
  },
  {
    "employeeNumber": 432156,
    "status": "RDO",
    "date": "26/04/19",
    "label": "0600-1800 CRT-CO"
  },
  {
    "employeeNumber": 7654674,
    "status": "Leave",
    "date": "30/03/20",
    "label": "1800-0600 CRT-CO"
  },
  {
    "employeeNumber": 123456,
    "status": "RDO",
    "date": "27/10/17",
    "label": "1800-0600 RO-CO"
  },
  {
    "employeeNumber": 123456,
    "status": "RDO",
    "date": "20/08/20",
    "label": "0800-2000 RO-CO"
  },
  {
    "employeeNumber": 432156,
    "status": "Working",
    "date": "01/11/19",
    "label": "0700-1900 CRT-SCO"
  },
  {
    "employeeNumber": 123456,
    "status": "RDO",
    "date": "22/03/17",
    "label": "0700-1900 TRAN-CO"
  },
  {
    "employeeNumber": 7654674,
    "status": "Working",
    "date": "11/11/20",
    "label": "1800-0600 TRAN-SCO"
  },
  {
    "employeeNumber": 7654674,
    "status": "RDO",
    "date": "18/06/18",
    "label": "0700-1900 RO-AVL"
  },
  {
    "employeeNumber": 432156,
    "status": "Working",
    "date": "24/02/20",
    "label": "1800-0600 CRT-CO"
  },
  {
    "employeeNumber": 123456,
    "status": "Working",
    "date": "21/03/20",
    "label": "0700-1900 RO-CO"
  },
  {
    "employeeNumber": 7654674,
    "status": "RDO",
    "date": "14/04/17",
    "label": "0600-1800 TRAN-SCO"
  },
  {
    "employeeNumber": 432156,
    "status": "Working",
    "date": "08/06/17",
    "label": "0600-1800 RO-SCO"
  },
  {
    "employeeNumber": 432156,
    "status": "Leave",
    "date": "28/11/17",
    "label": "1800-0600 RO-SCO"
  },
  {
    "employeeNumber": 7654674,
    "status": "RDO",
    "date": "04/05/20",
    "label": "0800-2000 CRT-CO"
  },
  {
    "employeeNumber": 123456,
    "status": "Working",
    "date": "17/02/18",
    "label": "1800-0600 RO-CO"
  },
  {
    "employeeNumber": 123456,
    "status": "Working",
    "date": "14/01/20",
    "label": "0800-2000 RO-CO"
  },
  {
    "employeeNumber": 123456,
    "status": "Leave",
    "date": "16/10/19",
    "label": "1800-0600 CRT-CO"
  },
  {
    "employeeNumber": 7654674,
    "status": "Working",
    "date": "25/01/18",
    "label": "1800-0600 RO-SCO"
  },
  {
    "employeeNumber": 7654674,
    "status": "Leave",
    "date": "09/03/18",
    "label": "0700-1900 RO-SCO"
  },
  {
    "employeeNumber": 123456,
    "status": "Leave",
    "date": "26/11/20",
    "label": "1800-0600 TRAN-SCO"
  },
  {
    "employeeNumber": 123456,
    "status": "Leave",
    "date": "11/06/19",
    "label": "1800-0600 TRAN-CO"
  },
  {
    "employeeNumber": 7654674,
    "status": "RDO",
    "date": "25/09/19",
    "label": "0700-1900 TRAN-CO"
  },
  {
    "employeeNumber": 432156,
    "status": "RDO",
    "date": "31/12/19",
    "label": "1800-0600 CRT-SCO"
  },
  {
    "employeeNumber": 7654674,
    "status": "RDO",
    "date": "30/07/17",
    "label": "1800-0600 RO-SCO"
  },
  {
    "employeeNumber": 123456,
    "status": "RDO",
    "date": "05/07/19",
    "label": "0700-1900 RO-SCO"
  },
  {
    "employeeNumber": 432156,
    "status": "Leave",
    "date": "29/09/20",
    "label": "0800-2000 CRT-CO"
  },
  {
    "employeeNumber": 432156,
    "status": "Leave",
    "date": "11/03/20",
    "label": "1800-0600 TRAN-CO"
  },
  {
    "employeeNumber": 123456,
    "status": "RDO",
    "date": "09/07/17",
    "label": "0800-2000 CRT-SCO"
  },
  {
    "employeeNumber": 7654674,
    "status": "Working",
    "date": "06/03/18",
    "label": "0600-1800 CRT-SCO"
  },
  {
    "employeeNumber": 432156,
    "status": "Leave",
    "date": "19/02/20",
    "label": "0800-2000 TRAN-SCO"
  },
  {
    "employeeNumber": 7654674,
    "status": "Working",
    "date": "20/02/19",
    "label": "1800-0600 RO-AVL"
  },
  {
    "employeeNumber": 7654674,
    "status": "Leave",
    "date": "18/03/18",
    "label": "1800-0600 TRAN-CO"
  },
  {
    "employeeNumber": 432156,
    "status": "Leave",
    "date": "16/08/17",
    "label": "0600-1800 CRT-SCO"
  },
  {
    "employeeNumber": 123456,
    "status": "RDO",
    "date": "16/06/18",
    "label": "0700-1900 CRT-CO"
  },
  {
    "employeeNumber": 432156,
    "status": "RDO",
    "date": "29/12/18",
    "label": "0700-1900 RO-AVL"
  },
  {
    "employeeNumber": 432156,
    "status": "Leave",
    "date": "03/11/17",
    "label": "1800-0600 TRAN-SCO"
  },
  {
    "employeeNumber": 7654674,
    "status": "Working",
    "date": "20/08/20",
    "label": "0800-2000 RO-CO"
  },
  {
    "employeeNumber": 432156,
    "status": "Working",
    "date": "03/01/17",
    "label": "0700-1900 RO-SCO"
  },
  {
    "employeeNumber": 123456,
    "status": "RDO",
    "date": "25/11/18",
    "label": "0600-1800 RO-AVL"
  },
  {
    "employeeNumber": 432156,
    "status": "RDO",
    "date": "25/04/17",
    "label": "0800-2000 RO-AVL"
  },
  {
    "employeeNumber": 7654674,
    "status": "Working",
    "date": "14/02/19",
    "label": "0600-1800 RO-AVL"
  },
  {
    "employeeNumber": 123456,
    "status": "Working",
    "date": "26/09/19",
    "label": "0700-1900 CRT-CO"
  },
  {
    "employeeNumber": 7654674,
    "status": "Working",
    "date": "28/04/18",
    "label": "0700-1900 RO-SCO"
  },
  {
    "employeeNumber": 432156,
    "status": "Working",
    "date": "09/04/20",
    "label": "0800-2000 RO-CO"
  },
  {
    "employeeNumber": 7654674,
    "status": "Working",
    "date": "11/01/17",
    "label": "1800-0600 RO-CO"
  },
  {
    "employeeNumber": 7654674,
    "status": "RDO",
    "date": "20/05/18",
    "label": "0600-1800 TRAN-CO"
  },
  {
    "employeeNumber": 432156,
    "status": "Working",
    "date": "03/12/19",
    "label": "0800-2000 RO-CO"
  },
  {
    "employeeNumber": 432156,
    "status": "Working",
    "date": "04/06/19",
    "label": "1800-0600 TRAN-SCO"
  },
  {
    "employeeNumber": 123456,
    "status": "Working",
    "date": "20/09/17",
    "label": "1800-0600 TRAN-CO"
  },
  {
    "employeeNumber": 7654674,
    "status": "Working",
    "date": "05/10/20",
    "label": "0800-2000 TRAN-SCO"
  },
  {
    "employeeNumber": 432156,
    "status": "Working",
    "date": "01/12/17",
    "label": "0700-1900 RO-AVL"
  }
]