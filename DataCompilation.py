from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)
# The user information
userName = None
userAddress = None
userID = None
dataBaseUser = None # var to check if the user is in the database
dataBasePassword = None # var to check if the user is correct
# The order information
userActiveOrder = None
orderRestaurant = None
orderTime = None

def user():
    global userName, userAddress, userID, dataBasePassword, dataBaseUser
def order():
    global userActiveOrderOrder, orderRestaurant, orderTime

# Getting the user data form the FE in login
@app.route('/login-form', methods=['GET', 'POST'])
def getUserData():
    error = None
    try:
        if request.method == "POST":
            attemptedUser = request.form["username"]
            attemptedPassword = request.form["password"]
            if attemptedUser == dataBaseUser and attemptedPassword == attemptedPassword:
                return redirect(url_for("restaurants"))
            else:
                error = "Invalid credentials. Try Again."
        return render_template("login-form", error = error)
    except Exception as e:
        return render_template("login-form", error = error)