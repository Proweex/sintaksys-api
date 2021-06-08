from flask import Flask, request
import json
import load_model
import os

app = Flask(__name__)
@app.route("/", methods=["GET"])
def jawab_get():
    jawaban={"message":"JSON post request tidak ada"}
    return json.dumps(jawaban)

@app.route("/", methods=['POST'])
def jawab_api():
    #request_json = request.get_json()
    if request.json["message"] is not None:
        kalimat = request.json["message"]
        hasil_predict = load_model.load(kalimat)
        jawaban = {
            "request" : request.json["message"],
            "message" : hasil_predict
        }
    
    else:
        jawaban = {
            "Error" : "NoneType object JSON request",
            "message" : "No JSON post request detected"
        }
    
    return json.dumps(jawaban)


if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# for testing purpose
#print(load_model.load("ini kaliat test yang ndak terlalu panjang"))