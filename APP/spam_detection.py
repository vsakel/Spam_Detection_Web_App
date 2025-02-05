from flask import Flask, render_template, request
import requests, os
from dotenv import load_dotenv


dotenv_path = "../.env"
# Load the .env file
load_dotenv(dotenv_path=dotenv_path,override=True)
# Access the environment variables
api_endpoint = os.getenv('API_ENDPOINT')

# # Initialize Flask app that will be the main app with frontend
app = Flask(__name__)

# Define route function for the welcome page
@app.route('/')
def home():
    return render_template('welcome.html')

# define route function
@app.route('/fill')
def fill():
    return render_template('fill.html')

@app.route('/prediction', methods=['POST','GET'])
def call_api():
    # if there is no POST request, there is no text input so we dont call the api, and render no_prediction.html 
    if request.method == 'POST':
        # Get form data
        language = request.form.get('lang')
        message = request.form.get('message')
        data={'lang': language, 'message': message} 
        response = requests.post(api_endpoint, json=data) # we will send data to API in json format
        if response.status_code == 200:
            print(f"Data successfully delivered, request code is: {response.status_code}")
            spam_prob = response.json().get("spam_probability")
            return render_template('prediction.html', prediction=spam_prob)
        print(f"Failed to deliver data, request code is: {response.status_code}")
    return render_template('no_prediction.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
