from flask import request
from . import app
from random import shuffle

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to the Family Friday webapp! Are you here to <a href='/register'>register</a> or <a href='/groups'>get</a> today's groups?"

@app.route('/register')
def register():
    return "Hi! Welcome to ApartmentList! What's your name, so we can get you all grouped up? <form method='post' action='/addname'><input type=text name='name'></input><input type=submit></input></form>"

@app.route('/addname', methods = ['POST', 'GET'])
def addname():
    form = request.form
    with open('names.csv', 'w') as f:
        f.write(str(form['name'])+'\n')
    return "Thanks for registering!"


@app.route('/groups')
def groups():
    names = []
    with open('names.csv', 'r') as f:
        for line in f:
            names.append(line.strip())
    shuffle(names)
    groups = [[names[x], names[x+1], names[x+2]] for x in [y * 3 for y in range(len(names) / 3)]]
    numstragglers = len(names) % 3
    print names[len(names)-numstragglers:]
    groups[-1] = groups[-1] + names[len(names)-numstragglers:]
    return "<div>Here are the groups for today, built from the following people: " + str(names) + ": " + str(len(names)) + " people.</div> <div>" + str(groups) + "</div>"
