from flask import Flask,request,render_template, redirect ,url_for, send_from_directory,Response,jsonify

app = Flask(__name__)

def calorieCalc():

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)