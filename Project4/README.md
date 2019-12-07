<h1>Blossom Academy Fall 2019 Cohort - Data Engineering</h1>

# Project Title

Basic ETL pipeline to read data from a source, transform this data, then load the output into a prescribed location

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install and have;


- Anaconda 
- Jupyter Notebook
- BeautifulSoup4
- lxml


### Installing

A step by step series of examples that tell you how to get a development env running

* Anaconda -  https://www.anaconda.com/distribution/ (Python 3.7 version)
* BeautifulSoup4 - pip install beautifulsoup4
* lxml - pip install lxml



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

