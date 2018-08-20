from app import app
from flask import render_template
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Brian'}
    projects = [
        {
            'number': 134,
            'name': 'Temple Villa Road',
            'type':'Rear Extension',
            'value': 400
        },
        {
            'number': 185,
            'name':   'Electric Ave.',
            'type':   'Loft Conversion',
            'value':  350
        },
    ]
    return render_template('index.html', title='Home', user=user, projects=projects)
    

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)