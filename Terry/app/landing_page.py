from flask import Flask, render_template, request
import requests
import pandas as pd
import requests


# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    
    return render_template("landing_page.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    make = 'Test make'
    model = 'Test model'
    year = 'Test year'
    vin = 'Test vin'
    num = 'Test plate num'
    state = 'Test state'
    img_url = projectpath

    # Return template and data
    return render_template("output_page.html", img_url=img_url, num=num, state=state, make=make, model=model, year=year, vin=vin)


if __name__ == "__main__":
    app.run(debug=True)
