from flask import Flask, render_template
import requests
import pandas as pd
import requests


# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    plate_input = '225NNJ'
    state_input = 'MN'
    url = "https://us-license-plate-to-vin.p.rapidapi.com/licenseplate"
    querystring = {"plate":plate_input,"state":state_input}
    headers = {
        'x-rapidapi-host': "us-license-plate-to-vin.p.rapidapi.com",
        'x-rapidapi-key': "<API KEY>"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    plate_data_df = pd.DataFrame(response.json())
    plate_data_dict = plate_data_df.to_dict()
    make = plate_data_dict['specifications']['make']
    model = plate_data_dict['specifications']['model']
    year = plate_data_dict['specifications']['year']
    vin = plate_data_dict['specifications']['vin']
    num = plate_data_dict['plate']['make']
    state = plate_data_dict['state']['make']
    img_url = "https://upload.wikimedia.org/wikipedia/commons/8/85/Minnesota_2014_License_Plate.jpg"

    # Return template and data
    return render_template("index_terry.html", img_url=img_url, num=num, state=state, make=make, model=model, year=year, vin=vin)

if __name__ == "__main__":
    app.run(debug=True)
