
from flask import *
from public import *
from admin import *
from hr import *
from staff import *
app = Flask(__name__)

app.secret_key="jfhtf"
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(hr)
app.register_blueprint(staff)

app.run(debug=True)