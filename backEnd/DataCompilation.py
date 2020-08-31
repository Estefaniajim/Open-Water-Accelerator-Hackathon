from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)
userName = None
userAddress = None
userID = None
userOrder = None

def user():
    global userName, userAddress, userID, userOrder

@app.route('/login-form', methods=['GET', 'POST'])
def getUserData():
    try:
    except Exception as e:
        return render_template("login-form", error = "There was a problem with the login information")




@app.route('/request-form', methods=['GET', 'POST'])
def getInfoOrder():



