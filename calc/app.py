# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

# Part 1
@app.route("/add")
def add_route(): 
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    sum = add(a,b)
    
    return str(sum)

@app.route("/sub")
def sub_route(): 
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    difference = sub(a,b)
    
    return str(difference)

@app.route("/mult")
def mult_route(): 
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    product = mult(a,b)
    
    return str(product)

@app.route("/div")
def div_route(): 
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    quotient = div(a,b)
    
    return str(quotient)


#Part 2
@app.route("/math/<operation>")
def math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    operators = {
        "add": add(a, b),
        "sub": sub(a, b),
        "mult": mult(a, b),
        "div": div(a, b)
    }

    result = operations[operators]

    return str(result)
