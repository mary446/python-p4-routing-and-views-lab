#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return f"<h1>{title}</h1>"

@app.route('/print/<string:str_parameter>')
def print_string(str_parameter):
    print('hello')  
    return f"hello"

@app.route('/count/<int:parameter>')
def count(parameter):
    result = '\n'.join(str(i) for i in range(1, parameter+ 1))
    return result

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    else:
        return "Invalid operation"

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
