# Project-4
For Project 4, we looked at Yelp data that we got directly from *Yelp.com* to analyze restaurants in the metropolitan areas.
## ETL Process
The first available data came from Kaggle reflecting Arizona Restaurants. We uploaded the dataset, *yelp_restaurant.csv* in an S3 bucket on AWS. Then we used PySpark to read in the data and ran our analysis.
* Used import tarfile and tarfile.open to extract .json files from the .tar file
* Then converted to CSV
* Dropped duplicates and nulls
* Dataset reflects metropolitan areas 
## Dataset 
* 8,635,403 reviews
* 160,585 businesses
* 8 metropolitan areas
* ~7GB of data
## Machine Learning Models Used
1. Logistic Regression
    * Conducted unscaled and scaled logistic regression
2. Random Forest 
    * Conducted a random forest, extra tree forest, and ensemble method
3. Deep Learning Neural Network
    * Conducted a two layer and keras tuner to get the best set of hyperparameters
## Presentation
The slide deck, *Project 4.pptx*, is in the Presentation Folder. It provides an overview of the purpose of the project, data preprocessing, and models used.
## Flask
The Flask application uses a virtual environment that contains all the necessary dependancies. It is host on AWS Elastic Beanstalk.
The Flask folder contains the *application.py* and all the necessary components to build the website.
## Yelp Analysis Website
Website can be found at this link:
http://yelpanalysis2-env-1.eba-vpvjzrm2.us-west-1.elasticbeanstalk.com/index.html 