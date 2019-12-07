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
- Postgresql
- Postgresql driver file
- DBeaver Community


### Installing

A step by step series of examples that tell you how to get a development env running

* Anaconda -  https://www.anaconda.com/distribution/ (Python 3.7 version)
* Amazon Simple Storage Service(S3) - https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
* Boto3 - pip install boto3
* Pyspark - pip install pyspark
* Postgresql - https://www.postgresql.org/download/
* Postgresql driver file - https://jdbc.postgresql.org/download.html (PostgreSQL JDBC 4.2 Driver, 42.2.8)
* DBeaver Community - https://dbeaver.io/download/


A recent version of Python is required, preferably 3.5 or 3.7.

### Setup
Setup the working environment on your computer, for instance Project-two.

Below are the steps to run commands:

1. Create a virtual env:
	* Using Python 3.5: `python3 -m venv project-three`
2. Activate the virtual env:
	* On Linux, MacOS, other UNIX: `source project-three/bin/activate`
	* On Windows: `project-three\Scripts\activate`
3. Install requirements: `pip install -r requirements.txt` 

### Tasks Performed
#### 1. DATA EXTRACTION:
      
1. Initialize spark with the following:

```
spark = (
    SparkSession.builder
                .appName("Stack Overflow Data Wrangling")
                .config("spark.jars", "C:\Users\USER\Desktop\Blossom_Academy\jars\postgresql-42.2.8.jar") 
                .getOrCreate()
)
```
2. Load the StackOverflow questions, answers and users datasets with pyspark
HINT: rename all id columns as you may encounter problems with multiple columns having the same name when you join several data frames.  Eg: Assuming you loaded the answers data into a variable called answers, rename this as follows,

`answers = answers.withColumnRenamed(‘id’, ‘answer_id’)`


#### 2. DATA TRANSFORMATION:
Assuming you have a folder on your computer named Blossom_Academy, create a new folder within this folder called jars then place this file into it.
1. Select users from only one country of your choosing.
2. Extract the country and city into new columns.
3. Join this with the questions and only pick questions with at least 20 view_counts.
4. Join the answers to the results of (3).

#### 3. DATA LOADING:
##### SQL DATA DEFINITION LANGUAGE(DDL)
1. Create a new schema called stackoverflow_filtered.
2. Create one table called results. 


#### DATA LOADING
3. Use spark to write the results into this table with the snippet below.
4. Create a btree index on the reputation column within the results table.
5. Create a hash index on the display_name column within the results table.
6. From the results table, create a view with the column names display_name, city, questions_id where the accepted_answer_id is not null. Make sure this view goes into the right schema.
7. Create a materialized view similar to (6). They should have different names.
8. In your Jupyter notebook, state the difference between views and materialized views.

#### 4. SQL DATA MANIPULATION LANGUAGE(DML)
1. How many cities appeared more than twice in your results table?
2. How many unique created_at dates(not datetime) are in the result table?
3. If you were to give an award to one user, who will it be? And why?

