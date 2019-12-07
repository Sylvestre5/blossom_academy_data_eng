<h1>Blossom Academy Fall 2019 Cohort - Data Engineering</h1>

# Project Title

Basic ETL pipeline to read data from a source, transform this data, then load the output into a prescribed location

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install and have;


- Anaconda 
- Amazon Simple Storage Service(S3)
- Boto3 client
- Amazon s3 account
- PySpark 
- Jupyter Notebook


### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be


* Anaconda -  https://www.anaconda.com/distribution/ (Python 3.7 version)
* Amazon Simple Storage Service(S3) - https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
* Boto3 - pip install boto3
* Pyspark - pip install pyspark

A recent version of Python is required, preferably 3.5 or 3.7.

### Setup
Setup the working environment on your computer, for instance Project-two.

Below are the steps to run commands:

1. Create a virtual env:
	* Using Python 3.5: `python3 -m venv project-two`
2. Activate the virtual env:
	* On Linux, MacOS, other UNIX: `source project-two/bin/activate`
	* On Windows: `project-two\Scripts\activate`
3. Install requirements: `pip install -r requirements.txt` 

### Tasks Performed

Create a Jupyter notebook that contains the following tasks:
- Load the data scientist job market dataset and us stocks datasets from the s3 bucket ‘s3://blossom-data-engs’ onto your computer
- Read the data with pyspark
     <p>* Read the alldata.csv from the data scientist datasets
- Join the 2 datasets.
- Write a function to generate n-grams (unigram & bigram) from a given text/description. 
- Write another function which uses the function from (c) to create 2 spark data frames which have 3 columns in the order of frequency: 
     <p>*{Ngram, City, Frequency}
     <p>*{Ngram, Industry, Frequency}
- Use any visualization to compare a role between 2 cities
- Commit this notebook into your github repo
