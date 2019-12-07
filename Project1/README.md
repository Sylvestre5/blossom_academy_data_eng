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


### Installing

A step by step series of examples that tell you how to get a development env running


* Anaconda -  https://www.anaconda.com/distribution/ (Python 3.7 version)
* Amazon Simple Storage Service(S3) - https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
* Boto3 - pip install boto3

A recent version of Python is required, preferably 3.5 or 3.7.

### Setup
Setup the working environment on your computer, for instance Project-two.

Below are the steps to run commands:

1. Create a virtual env:
	* Using Python 3.5: `python3 -m venv project-three`
2. Activate the virtual env:
	* On Linux, MacOS, other UNIX: `source project-four/bin/activate`
	* On Windows: `project-three\Scripts\activate`
3. Install requirements: `pip install -r requirements.txt` 

### Tasks Performed
- Write a python script with the following features; 
    <p>a. Download the 7+ Million Dataset from S3 [bucket: blossom-data-engs key:-project1/free-7-million-company-dataset.zip].</p>
    <p>b. Read the file with pandas.</p>
    <p>c. Filter out companies without a domain name using pandas.</p>
    <p>d. Write out the output(from point c.) in the following formats;</p>
          <p> - Parquet</p>
          <p> - JSON (compressed using gzip)</p>
          <p> - AVRO</p>
- Upload the resulting 3 file to your S3 buckets blossom-data-eng-[student-name].
- Commit your code to your github repository.


