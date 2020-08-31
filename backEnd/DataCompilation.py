from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)
userName = None
userAddress = None
userID = None
userOrder = None
dataBaseUser = None
dataBasePassword = None

def user():
    global userName, userAddress, userID, userOrder, dataBasePassword, dataBaseUser

@app.route('/login-form', methods=['GET', 'POST'])
def getUserData():
    error = None
    try:
        if request.method == "POST":
            attemptedUser = request.form["username"]
            attemptedPassword = request.form["password"]
            if attemptedUser == dataBaseUser and attemptedPassword == attemptedPassword:
                return redirect(url_for("restaurants"))
    except Exception as e:
        return render_template("login-form", error = error)




@app.route('/request-form', methods=['GET', 'POST'])
def getInfoOrder():



