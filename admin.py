

from flask import *
from database import *
admin=Blueprint('admin',__name__)
@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')
@admin.route('/managehr',methods=['POST','GET'])
def managehr():
    if 'submit' in request.form:
        hrm  = request.form['hrnm']
        quali = request.form['quali']
        phone = request.form['phone']
        email = request.form['em']
        username = request.form['uname']
        password = request.form['passw']
        mhrlogin = "insert into login values(null,'%s','%s','hr')"%(username,password)
        res = insert(mhrlogin)
        mhrreg = "insert into hr_team values(null,'%s','%s','%s','%s','%s')"%(res,hrm,quali,phone,email)
        insert(mhrreg)
    data = {}
    qry5 = "select * from hr_team"
    
  
    data['hr'] = select(qry5) 

    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']

    else:
        action = None

    if action=='delete':
        qry8 = "delete from hr_team where hr_id='%s'"%(id)
        delete(qry8)
        return redirect(url_for('admin.managehr'))
    if action=='update':
        qry0="select * from hr_team where hr_id='%s'"%(id)
        data['up'] = select(qry0)


    if 'update' in request.form:
        name = request.form['name']
        qualification = request.form['quali']
        phone = request.form['phone']
        email = request.form['email']
        # pnum = request.form['pnum']
        # desig_id = request.form['desig']
        # em = request.form['ema']
        qryup = "update hr_team set name='%s', qualification='%s', phone='%s', email='%s'  where hr_id='%s'"%(name,qualification,phone,email,id)
        update(qryup)
        return redirect(url_for('admin.managehr'))

        


    return render_template('managehr.html',data=data)

@admin.route('/managedesighnation')
def managedesighnation():
    
    return render_template('manage_desighnation.html')



@admin.route('/managestaff',methods=['POST','GET'])
def managestaff():
    data = {}
    qry2 = "select * from designation"
    item=select(qry2)
    data['view'] = item

    if 'submit' in request.form:
        fname = request.form['fname']
        lastname = request.form['lname']
        gender = request.form['gender']
        dob = request.form['dob']
        pnum = request.form['pnum']
        desig_id = request.form['desig']
        em = request.form['ema']

        uname = request.form['uname']
        passw = request.form['passw']
        qry = "insert into login values(null,'%s','%s','staff')"%(uname,passw)
        res = insert(qry)
        qry3 = "insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,desig_id,fname,lastname,gender,dob,pnum,em)
        insert(qry3)

     
    qry5 = "select * from staff"
    
  
    data['staff'] = select(qry5) 

    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']

    else:
        action = None

    if action=='delete':
        qry8 = "delete from staff where staff_id='%s'"%(id)
        delete(qry8)
        return redirect(url_for('admin.managestaff'))
    if action=='update':
        qry0="select * from staff where staff_id='%s'"%(id)
        data['up'] = select(qry0)


    if 'update' in request.form:
        fname = request.form['fname']
        lastname = request.form['lname']
        gender = request.form['gender']
        dob = request.form['dob']
        pnum = request.form['pnum']
        desig_id = request.form['desig']
        em = request.form['ema']
        qryup = "update staff set first_name='%s', last_name='%s', gender='%s', dob='%s', phone='%s', email='%s'  where staff_id='%s'"%(fname,lastname,gender,dob,pnum,em,id)
        update(qryup)


        


    return render_template('managestaff.html',data=data)



@admin.route('/sendnotification',methods=['POST','GET'])
def sendnotity():
    if 'submit' in request.form:
        nd = request.form['nd']
        qrynot = "insert into notification values(null,'%s',curdate())"%(nd)
        insert(qrynot)



    return render_template('sendnotification.html')
@admin.route('/viewattendance',methods=['POST','GET'])
def attendance():
    data = {}
    attendqry = "select * from attendance"
    data['view'] = select(attendqry)
    return render_template('viewattendance.html',data=data)
@admin.route('/viewcomplaints',methods=['POST','GET'])
def viewcomplaints():
    data = {}
    complaintqry = 'select * from complaints'
    data['view'] = select(complaintqry)
   
    
    return render_template('viewcomplaints.html',data=data)


@admin.route('/viewhr',methods=['POST','GET'])
def viewhr():
    data = {}
    vhr = "select * from hr_team"
    data['view'] = select(vhr)
    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']

    else:
        action = None

    if action=='delete':
        qry8 = "delete from hr_team where hr_id='%s'"%(id)
        delete(qry8)
        return redirect(url_for('admin.viewhr'))
    if action=='update':
        qry0="select * from hr_team where hr_id='%s'"%(id)
        data['up'] = select(qry0)


    if 'update' in request.form:
        fname = request.form['fname']
        quali = request.form['quali']
        phone = request.form['phone']
        email = request.form['ema']
        
        qryup = "update hr_team set name='%s', qualification='%s',phone='%s',  email='%s'  where hr_id='%s'"%(fname,quali,phone,email,id)
        update(qryup)

    return render_template('viewhr.html',data=data)
@admin.route('/adminsendreply',methods=['POST','GET'])
def adminsendreply():
 if 'submit' in request.form:
     reply = request.form['reply']
     id = request.args['id']
     relpqry = "update complaints set reply='%s' where complaints_id='%s'"%(reply,id)
     update(relpqry)
     return redirect(url_for('admin.viewcomplaints'))
 return render_template('adminsendreply.html')
@admin.route('/logout',methods=['POST','GET'])
def logout():
    return redirect(url_for('public.login'))




  
    
















