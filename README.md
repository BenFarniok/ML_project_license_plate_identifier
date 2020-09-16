## Plate Reader Project

The project contained within the "Heroku App" folder functions as a tool to find information about a vehicle from a picture of a license plate.

The deployment to Heroku is not currently active, due to memory concerns and costs associated with API calls.

However, the code contained within the Flask app contained within the folder is functional and does work within a virtual environment.


## How to run the program

Relevant installs: OpenCV, Tensorflow, Keras, Python 3.6, NumPy and Sci-kit Learn.

Upon starting the Flask app in Git Bash and visiting the associated page (which will be available in your console), you will be presented with a webpage.

This webpage will have an option to upload in image on the right-hand side, (an example image is provided in Plate_examples) the webpage will take that image, process it, and using a pre-built deep-learning model, attempt to identify the letters on a license plate.

Currently, the reader is only set up to access information about Minnesotan license plates, but the machine learning model is also able to read and identify the characters on license plates from other states.
Further functionality is planned to be added in coming weeks to allow more robust usage for the product.

Once finished with the project, one can close out the Flask app by hitting 'CTRL+C' in the console window where the Flask app is running.



## How the the machine learning component works:

The projects work with machine learning is the lynchpin to this entire project, and understanding it is key to understanding the work that went in to making it functional.

![landing_page](https://github.com/BenFarniok/ML_project_license_plate_identifier/raw/master/Images/starting_page.jpg)

Upon the introduction of the image, the html passes the image to the Flask App using the "POST" method, which will run the 'plate_reader' function.

There-in, converted into an array format that is legible to OPENCV, which begins to process the image. First, it will search for license plates in the image by looking for rectangular shapes that would match a profile of a plate.

![plate_finder](https://github.com/BenFarniok/ML_project_license_plate_identifier/raw/master/Images/plate_finder.jpg)

Then will render the image into greyscale and blurry before using adaptive binarization to render it into black and white.

![processing](https://github.com/BenFarniok/ML_project_license_plate_identifier/raw/master/Images/plate_processor.jpg)

From there, the newly-binarized image is looked over for countours that occupy atleast 40 percent of the identified plates height, assuming those will be characters.

![contour](https://github.com/BenFarniok/ML_project_license_plate_identifier/raw/master/Images/countour_finder.jpg)

After that, it applies the pre-built model "wpod-net" which was trained on a series of binarized images to identify characters.

![binarized](https://github.com/BenFarniok/ML_project_license_plate_identifier/raw/master/Images/separated_characters.jpg)

The "plate_reader" function returns a string to the Flask app, which is used to make an API call to identify the Vehicle Identification Number (VIN).

![final_result](https://github.com/BenFarniok/ML_project_license_plate_identifier/raw/master/Images/final_result.jpg)

This VIN, in turn, is used to retrieve information about the make, model and year of the vehicle.

![returned_page](https://github.com/BenFarniok/ML_project_license_plate_identifier/raw/master/Images/returned.jpg)

With further development, the web-app could also be used to find further information about the vehicle, including Kelly Blue Book value and accident history.
