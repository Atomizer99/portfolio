from flask import Flask,request,render_template,jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://db:27017/')
db = client.calocalc_database
collection = db.calocalc_collection
users = db.users



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
    user = {
        "firstname": request.form.get('fname'),
        "lastname": request.form.get('lname'),
        "age": request.form.get('Age'),
        "sex": request.form.get('Sex'),
        "height": request.form.get('Height'),
        "weight": request.form.get('Weight'),
        "BMR": BMR,
        "cals": cals
    }
    user_id = users.insert_one(user)
    return "Your BMR is: " + str(BMR) + "." + "<br>Your daily calorie intake should be at least: " + str(cals) + "."
    
@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)