# Import the redirect function
from flask import Flask, request, render_template
import model


# Initialize your Flask app
app = Flask(__name__)
# Render the HTML page with the form
@app.route('/')
def explore():
    return render_template('v.html')

@app.route('/index')
def index():
    return render_template('index.html')

# Get user input and make the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Your code to get user input and predict the price
    input_features = [x for x in request.form.values()]
    bath = input_features[0]
    balcony = input_features[1]
    total_sqft_int = input_features[2]
    bhk = input_features[3]
    area_type = input_features[4]
    availability = input_features[5]
    location = input_features[6]
     
    # predict the price of house by calling model.py
    predicted_price = model.predict_house_price(bath,balcony,total_sqft_int,bhk,area_type,availability,location) 


    return render_template('index.html', prediction_text='{} lakhs'.format(predicted_price))

# Run the Flask app
if __name__ == "__main__":
    app.run()
