from flask import Flask
from flask import url_for
from flask import redirect
from flask import request
from flask import render_template

# Flask is a python class
# We are going to create an instance of the Flask Class
# and assign it to a variable
# We can also say, creating an object of Flask Class
app = Flask(__name__)

# In flask functions are decorated by @app.route
# route is the mapping of url to python function
# If anybody request / then Hello World is sent as response to the browser
@app.route("/")
def hello_world():
    return """
        <html>
        <head><title>Hello World</title></head>
        <body>
            <h1>Hello World</h1>
            <a href="/products">Products</a>
        </body>
        </html>
    """

@app.route("/products")
def products():
    return """
        <html>
        <head><title>Products</title></head>
        <body>
            <ol>
                <li>Television</li>
                <li>Radio</li>
            </ol>
            <a href="/">Home</a>
        </body>
        </html>
    """

# Passing arguments to our function using URL
# URL http://127.0.0.1:5000/greeting/john
# greeting refers to the function john is an argument => greeting("john")
# the route configuration will be /greeting/<name>
@app.route("/greeting/<name>")
def greeting(name):
    return f"""
        <html>
        <head><title>Products</title></head>
        <body>
            Hello {name}, Welcome to Flask Tutorial
            <a href="/">Home</a>
        </body>
        </html>
    """

# the parameters are always string
# @app.route("/simpleinterest/<principle>/<period>/<rate>")
@app.route("/simpleinterest/<int:principle>/<int:period>/<int:rate>")
@app.route("/calculatesimpleinterest/<int:principle>/<int:period>/<int:rate>")
@app.route("/simpleinterest/<int:principle>/<int:period>", defaults={'rate': 6})
@app.route("/simpleinterest/<int:principle>", defaults={'period':1, 'rate': 6})
def simpleInterest(principle, period, rate):
    # interest = (int(principle) * int(period) * int(rate)) / 100
    interest = (principle * period * rate) / 100
    return f"""
        <html>
        <head><title>Products</title></head>
        <body>
            <table>
                <tr>
                    <td>Principle:</td><td>{principle}</td>
                </tr>
                <tr>
                    <td>Period:</td><td>{period}</td>
                </tr>
                <tr>
                    <td>Rate:</td><td>{rate}</td>
                </tr>
                <tr>
                    <td>Interest Amount:</td><td>{interest}</td>
                </tr>
                <tr>
                    <td>Total Amount to be Paid:</td><td>{interest + principle}</td>
                </tr>
            </table>
            <a href="/">Home</a>
        </body>
        </html>
    """

@app.route('/demoredirect')
def demoredirect():
    return redirect(url_for('greeting', name="Peter"))

@app.route('/login')
def login():
    return """
        <html>
            <head><title>Login</title></head>
            <body>
                <form action="/verifylogin" method="post">
                    <input type="text" name="emailaddress" id="emailaddress"/>
                    <input type="password" name="password" id="password"/>
                    <input type="submit" name="submitbtn" value="Login"/>
                </form>
            </body>
        </html>
    """

# instead of using route let us use specific method post
@app.post('/verifylogin')
def verifylogin():
    emailaddress = request.form['emailaddress']
    password = request.form['password']
    if (emailaddress == "admin@gmail.com" and password == "pwd123"):
        return f"""
            <html>
                <head><title>Verify Login</title></head>
                <body>
                    <h2>Verify Login</h2>
                    <h6>Email Address: { request.form['emailaddress'] }</h6>
                    <h6>Password: { request.form['password'] }</h6>
                </body>
            </html>
        """
    else:
        return redirect(url_for('login'))
    
@app.route("/goodlookinglogin")
def goodLookingLogin():
    return render_template('login.html')