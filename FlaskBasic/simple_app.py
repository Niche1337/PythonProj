from flask import Flask
from flask import render_template
#from flask import request

app = Flask(__name__)


####Route decorator
@app.route('/')
@app.route('/<name>')
def index(name="Teshy"):
    ##name now comes from the route
    ##name = request.args.get('name', name)
    return render_template("index.html", name=name)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
    return render_template("add.html", num1=num1, num2=num2)
    #.format(num1, num2, num1 + num2)
    
    

app.run(debug=True)