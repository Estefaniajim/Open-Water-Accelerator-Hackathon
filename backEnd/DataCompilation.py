from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)
userName = None
userAddress = None
userID = None
userActiveOrder = None
dataBaseUser = None
dataBasePassword = None
orderRestaurant = None
orderTime = None

def user():
    global userName, userAddress, userID, dataBasePassword, dataBaseUser
def order():
    global userActiveOrderOrder, orderRestaurant, orderTime

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