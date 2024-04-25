
from flask import *
from database import *
from hr import *
from staff import *
from admin import *

public=Blueprint('public',__name__)
@public.route('/')
def home():
    return render_template('home.html')
@public.route('/login',methods=['POST','GET'])
def login():
    if 'submit' in request.form:
       uname = request.form['uname']
       passw = request.form['passw']
       qry="select * from login where username='%s' and password='%s'"%(uname,passw)
       res = select(qry)
       print(res)
       
       session['lid']=res[0]['login_id']
       if res[0]['usertype']=='hr':
            qry8="select * from hr_team where login_id='%s'"%(session['lid'])
            res=select(qry8)
            session['hr']=res[0]['hr_id']
          
            return redirect(url_for('hr.hrhome'))
       if res[0]['usertype'] == 'staff':
           a="select * from staff where login_id='%s'"%(session['lid'])
           ss=select(a)
           session['sid']=ss[0]['staff_id']
           return redirect(url_for('staff.staffhome'))
       if res[0]['usertype'] == 'admin':
           return redirect(url_for('admin.adminhome'))



    return render_template('login.html')











