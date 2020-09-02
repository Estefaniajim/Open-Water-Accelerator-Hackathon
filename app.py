from flask import Flask, render_template, request
from flas
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        #Fetch form data
        userDetails = request.form
        name = userDetails["name"]
        email = userDetails["email"]
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)