from flask import Flask,render_template,request,make_response
from flask import json
from flask.json import jsonify
from flask_cors import CORS
import json
import pandas as pd
from pycaret.regression import load_model, predict_model


app = Flask(__name__)
CORS(app)
key = "rwg2nilbso05ak918xcz" # Generated from randomkey program
model = load_model('final_model')

def create_bad_request(data):
    return make_response(jsonify(data),400)

def make_ok_request(data):
    return make_response(jsonify(data),200)

@app.route("/",methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/api",methods = ["POST"])
def API():
    data = json.loads(request.data)
    if "key" not in list(data.keys()):
        return make_response(jsonify({
            "message" : "You are Unauthorized!!!"
        }),403)
    elif data["key"] != key:
        return make_response(jsonify({
            "message" : "You are Unauthorized!!!"
        }),403)


    if 'ENCOUNTERS' not in list(data.keys()):
        return create_bad_request({"message" : "ENCOUNTERS is Missing! "})
    elif "ENCOUNTER_DURATION" not in list(data.keys()):
        return create_bad_request({"message" : "ENCOUNTER_DURATION is Missing!"})
    elif "DOSES" not in list(data.keys()):
        return create_bad_request({"message" : "DOSES is Missing ! "})
    elif "DISPENSES" not in list(data.keys()):
        return create_bad_request({"message" : "DISPENSES is Missing!"})
    elif "Total Course Duration" not in list(data.keys()):
        return create_bad_request({"message" : "Total Course Duration is Missing!"})
    elif "PROCEDURES" not in list(data.keys()):
        return create_bad_request({"message" : "PROCEDURES is Missing !"})
    elif "Allergies + Conditions" not in list(data.keys()):
        return create_bad_request({"messsage" : "Allergies + Conditions is Missing !"})
    elif "HEALTHCARE_EXPENSES + HEALTHCARE_COVERAGE" not in list(data.keys()):
        return create_bad_request({"message" : "HEALTHCARE_EXPENSES + HEALTHCARE_COVERAGE is Missing !"})
    elif "TOTAL_CALCULATED_COST" not in list(data.keys()):
        return create_bad_request({"message" : "TOTAL_CALCULATED_COST is Missing!"})
    else : 
        try : 
            dict_data = {}
            for elem in list(data.keys()):
                if elem != "key":
                    temp = [data[elem],]
                    dict_data[elem] = temp
            df = pd.DataFrame(data = dict_data)
            predictions = predict_model(model, data=df)
            label = predictions["Label"][0]
            message = "" 
            if label == 1: 
                message = "Upto 25%"
            elif label == 3: 
                message = "Upto 50%"
            elif label == 2:
                message = "Upto 75%"
            else : 
                message = "Upto 100%"

            return make_ok_request({
                "group" : int(label),
                "message" : message

            })
        except:
            return make_response(jsonify({
                "message" : "Data Recieved was not proper!"
            }),400)

if __name__ == '__main__':
    app.run(debug=True)