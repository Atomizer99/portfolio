from flask import Flask,request,render_template, redirect ,url_for, send_from_directory,Response,jsonify
from flask_pymongo import PyMongo

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

app = Flask(__name__)

@app.route('/calculate', methods=["POST"])
def BMRCalc():
    Sex = request.form.get('Sex')
    Height = float(request.form.get('Height'))
    Weight = float(request.form.get('Weight'))
    Age = int(request.form.get('Age'))
    BMR = 0
    cals = 0
    print(Sex)
    if Sex == "Male":
        BMR = (10 * Weight) + (6.25 * Height) - (5 * Age) + 5
        cals = BMR * 1.2
    elif Sex == "Female":
        BMR = (10 * Weight) + (6.25 * Height) - (5 * Age) - 161
        cals = BMR * 1.2
    return "Your BMR is: " + str(BMR) + "." + "<br>Your daily calorie intake should be at least: " + str(cals) + "."

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)