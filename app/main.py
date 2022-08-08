
from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def cool_form():
    if request.method == "POST":
        if ("login" in request.form):
            return redirect(url_for("driver_login"))
        if ("register" in request.form):
            return redirect(url_for("driver_register"))

@app.route("/login",methods = ["GET", "POST"])
def driver_login():
    hint = "please login"
    return render_template("login.html", hint=hint)

@app.route("/register", methods = ["GET", "POST"])
def driver_register():
    hint = "please register"
    return render_template("register.html", hint=hint)

if __name__ == '__main__':
    app.run(host="0.0.0.0")


