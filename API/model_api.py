from model_func import model_logic
from flask import Flask, request, jsonify, render_template

# # Initialize the model API, that will expose the model in our frontend 
# so we can use models prediction in users text messages

app = Flask(__name__)

@app.route("/")
def hello_api():
    return render_template('welcome_api.html')


@app.route('/api_prediction', methods=['POST'])
def predict():
    data = request.json # This captures the JSON data sent in the request 
    language = data.get('lang') # extract 'lang' from the json data 
    message = data.get('message') # extract 'message' from the json data
    prob_spam = model_logic(language,message)
    return jsonify({"spam_probability": prob_spam})  # Return the float as JSON


if __name__ == '__main__':
    app.run(debug=True,port=5001)