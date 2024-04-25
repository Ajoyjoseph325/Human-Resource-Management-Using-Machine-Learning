from flask import *
from database import *
from public import *
staff = Blueprint('staff',__name__)
@staff.route('/staffhome',methods=['POST','GET'])
def staffhome():
    return render_template('staffhome.html')
@staff.route('/viewprofile',methods=['GET','POST'])
def viewprofile():
    data = {}
    pqry = "select * from staff where staff_id='%s'"%(session['sid'])
    data['staff']=select(pqry)

    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']

    else:
        action = None

    if action=='update':
        qry0="select * from staff where staff_id='%s'"%(id)
        data['up'] = select(qry0)


    if 'update' in request.form:
        fname = request.form['fname']
        lastname = request.form['lname']
        gender = request.form['gender']
        dob = request.form['dob']
        pnum = request.form['pnum']
        em = request.form['ema']
        qryup = "update staff set first_name='%s', last_name='%s', gender='%s', dob='%s', phone='%s', email='%s'  where staff_id='%s'"%(fname,lastname,gender,dob,pnum,em,id)
        update(qryup)
        return redirect(url_for('staff.viewprofile'))

    return render_template('viewprofile.html',data=data)
@staff.route('/changepassword',methods=['POST','GET'])
def changepassword():
    if 'submit' in request.form:
        npassw = request.form['npassw']
        passqry = "update login set password='%s' where login_id='%s'"%(npassw,session['lid'])
        update(passqry)
        return redirect(url_for('staff.viewprofile'))

    return render_template('changepassword.html')

@staff.route('/sendcomplaintstaff',methods=['POST','GET'])
def sendcomplaints():
    data = {}
    staff="select * from staff"
    data['view']=select(staff)
    if 'submit' in request.form:
        complaint = request.form['complaint']
        # staff_id = request.form['staff']
        
        cqry = "insert into complaints values(null,'%s','%s','null',curdate())"%(session['sid'],complaint)
        insert(cqry)
        return redirect(url_for('staff.staffhome'))
    return render_template('sendcomplaintstaff.html',data=data)

@staff.route('/logout',methods=['POST','GET'])
def logout():
    return redirect(url_for('public.login'))

    




    
