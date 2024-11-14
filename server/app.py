#!/usr/bin/env python3

from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<body>
    {% if title %}
    <h1>{{ title }}</h1>
    {% endif %}
    {% if content %}
    <p>{{ content }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, 
        title="Python Operations with Flask Routing and Views")

@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Console output
    return render_template_string(HTML_TEMPLATE, content=text)

@app.route('/count/<int:number>')
def count(number):
    result = '\n'.join(str(i) for i in range(number))
    return render_template_string(HTML_TEMPLATE, content=result)

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        'div': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }
    
    if operation not in operations:
        return "Invalid operation", 400
    
    try:
        result = operations[operation](num1, num2)
        return render_template_string(HTML_TEMPLATE, 
            content=f"{num1} {operation} {num2} = {result}")
    except ZeroDivisionError:
        return "Cannot divide by zero", 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)