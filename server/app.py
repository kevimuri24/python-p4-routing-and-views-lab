from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:number>')
def count(number):
    return '\n'.join(str(n) for n in range(number)) + '\n'

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
   
   if result is not None:
       return str(result)
   return "Invalid operation", 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)