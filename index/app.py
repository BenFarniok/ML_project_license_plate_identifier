from flask import Flask, render_template
import requests
import pandas as pd
import requests,json


# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
    post_fields = {'format': 'json', 'data':'1FVACWDU1BHBB3474'}
    vin_data = requests.post(url, data=post_fields)
    vin_data_df = pd.DataFrame(vin_data.json()['Results'])
    vin_data_dict = vin_data_df.to_dict()
    vin_data_dict

    make = vin_data_dict['Make'][0]
    model = vin_data_dict['Model'][0]
    year = vin_data_dict['ModelYear'][0]
    bodyclass = vin_data_dict['BodyClass'][0]
    drivetype = vin_data_dict['DriveType'][0]
    cylinders = vin_data_dict['EngineCylinders'][0]
    fuel_type = vin_data_dict['FuelTypePrimary'][0]
    vin = vin_data_dict['VIN'][0]

    img_url = "https://upload.wikimedia.org/wikipedia/commons/8/85/Minnesota_2014_License_Plate.jpg"
    num = '[dummy num]'
    state = '[dummy state]'
    price = '[dummy price]'

    # Return template and data
    return render_template("index.html", img_url=img_url, num=num, state=state, make=make, model=model, year=year, price=price, vin=vin)

if __name__ == "__main__":
    app.run(debug=True)
