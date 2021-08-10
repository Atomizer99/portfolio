from flask import Flask,request,render_template, redirect ,url_for, send_from_directory,Response,jsonify
from flask_pymongo import PyMongo

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

app = Flask(__name__)

@app.route('/calculate', methods=["POST"])
def BMRCalc():
    Sex = request.args.get('Sex')
    Height = request.args.get('Height')
    Weight = request.args.get('Weight')
    Age = request.args.get('Age')
    BMR = 0
    cals = 0
    print(Sex)
    if Sex == "Male":
        BMR = (10 * Weight) + (6.25 * Height) - (5 * Age) + 5
        cals = BMR * 1.2
    elif Sex == "Female":
        BMR = (10 * Weight) + (6.25 * Height) - (5 * Age) - 161
        cals = BMR * 1.2
    return "Your BMR is" + str(BMR) + "\nYour daily calorie intake shoudl be at least" + str(cals) + "."

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)