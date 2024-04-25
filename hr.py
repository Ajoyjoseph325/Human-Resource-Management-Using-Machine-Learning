from flask import *
from database import *
from ml import *
hr=Blueprint('hr',__name__)


@hr.route('/hrhome',methods=['POST','GET'])
def hrhome():
  

    return render_template('hrhome.html')

@hr.route('/viewnotifications',methods=['POST','GET'])
def viewnotification():
    data = {}
    notqry = "select * from notification"
    data['view'] =  select(notqry)

    return render_template('viewnotifications.html',data=data)


@hr.route('/sendcomplaints',methods=['POST','GET'])
def sendcomplaints():
    data = {}
    staff="select * from staff"
    data['view']=select(staff)
    if 'submit' in request.form:
        complaint = request.form['complaint']
  
        
        cqry = "insert into complaints values(null,'%s','%s','pending',curdate())"%(session['hr'],complaint)
        insert(cqry)
        return redirect(url_for('hr.hrhome'))
    return render_template('sendcomplaintshr.html',data=data)
@hr.route('/viewreply',methods=['POST','GET'])
def viewreply():
    data = {}
    vr = "select * from complaints"
    data['view'] = select(vr)
    
    return render_template('viewreply.html',data=data)
@hr.route('/viewattendance',methods=['POST','GET'])
def viewattendance():
    pass
@hr.route('/logout',methods=['POST','GET'])
def logout():
    return redirect(url_for('public.login'))



@hr.route('/prediction', methods=['POST', 'GET'])
def prediction():
    data = {}
    a = "select * from staff"
    res = select(a)
    data['view'] = res

    prediction_result = None  # Define prediction_result outside the if block

    if 'submit' in request.form:
        stf = request.form['stf']
        sl = float(request.form['sl'])
        le = float(request.form['le'])
        np = int(request.form['np'])
        amh = int(request.form['amh'])
        tsc = int(request.form['tsc'])
        wa = int(request.form['wa'])
        promo = int(request.form['promo'])
        dept = request.form['dept']
        sal = request.form['sal']

        user_input = {
            
            'satisfaction_level': sl,
            'last_evaluation': le,
            'number_project': np,
            'average_montly_hours': amh,
            'time_spend_company': tsc,
            'Work_accident': wa,
            'promotion_last_5years': promo,
            'department': dept,
            'salary': sal
        }

        prediction_result = predict_employee_leave(user_input)

    return render_template("predict.html", data=data, prediction_result=prediction_result)




