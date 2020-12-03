from flask import make_response, request, render_template, url_for, jsonify, redirect, session
from website.app import app
from src.make_inference import interact_model
import json

'''
return GLUCOSE inference given user's request

request: 
    data: contain json file that stores:
        antecedent: user-specified antecedent
        dimension: user-specified dimension
        story: the story that this inference is about
        nsamples: the number of samples that user requests
        spec_general: whether model generate specific or general knowledge inference
'''
@app.route('/request_inference', methods=["POST"])
def request_inference():
    data = request.get_json()
    print("request inference")
    raw_text = data['story']+"#"+data['antecedent']+"#"+data['dimension']+"#"
    ans_list = interact_model(nsamples=int(data['nsamples']), raw_text=raw_text)
    return json.dumps({"answer-list": ans_list})

@app.route('/')
def index():
    print("hello world")
    return make_response(render_template('index.html', css=url_for('static', filename="css/main.css")))

if __name__ == "__main__":
    app.run(debug=True)
