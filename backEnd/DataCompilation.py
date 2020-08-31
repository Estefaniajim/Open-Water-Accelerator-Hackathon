from flask import Flask, request, url_for, redirect

app = Flask(__name__)
userName = None
userAddress = None
userID = None
userOrder = None

def user():
    global userName, userAddress, userID, userOrder

@app.route('/login-form', methods=['GET', 'POST'])
def getUserData():


@app.route('/request-form', methods=['GET', 'POST'])
def getInfoOrder():



