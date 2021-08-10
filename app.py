from flask import Flask,request,render_template, redirect ,url_for, send_from_directory,Response,jsonify

app = Flask(__name__)

@app.route('/calculate', methods=["POST"])
def BMRCalc():
    Sex = request.args.get('Sex')
    Height = request.args.get('Height')
    Weight = request.args.get('Weight')
    Age = request.args.get('Age')
    if Sex == "Male":
        BMR = (10 * Weight) + (6.25 * Height) - (5 * Age) + 5
        cals = BMR * 1.2
    if Sex == "Female":
        BMR = (10 * Weight) + (6.25 * Height) - (5 * Age) - 161
        cals = BMR * 1.2
    return "Your BMR is" + BMR + "\nYour daily calorie intake shoudl be at least" + cal + "."

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)