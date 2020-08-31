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
    error = None
    try:
        if request.method == "POST":
            attemptedUser = request.form["username"]
            attemptedPassword = request.form["password"]
            

    except Exception as e:
        return render_template("login-form", error = error)




@app.route('/request-form', methods=['GET', 'POST'])
def getInfoOrder():



