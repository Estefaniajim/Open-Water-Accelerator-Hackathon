from flask import Flask, request, url_for, redirect, render_template
from flask_mysqldb import MySQL
import yaml

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

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

def user():
    global userName, userAddress, userID, dataBasePassword, dataBaseUser
def order():
    global userActiveOrderOrder, orderRestaurant, orderTime

#Registering a new user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirmPass = request.form["confirmPass"]
        error = None
        cur = mysql.connection.cursor()
    if not username:
        error = "Username is required."
    elif not password:
        error = "Password is required."
    elif password != confirmPass:
        error = "Passwords do not match."

    if error is None:
        cur.execute("INSERT INTO users(username, email, password) VALUES(%s, %s, %s)",(name, email, password))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("address"))

    return render_template("register", error = error)

#Adding address details
@app.route("/address", methods=["GET", "POST"])
def address():
    if request.method == "POST":
        address1 = request.form["address1"]
        address2 = request.form["address2"]
        city = request.form["city"]
        state = request.form["state"]
        zipCode = request.form["zipCode"]
        cur.execute("INSERT INTO users(address1, address2, city, state, zipCode) VALUES(%s, %s, %s, %s, %s)",
                   (address1, address2, city, state, zipCode))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("auth.login"))

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
