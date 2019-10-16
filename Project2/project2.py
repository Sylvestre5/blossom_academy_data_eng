
from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from pyspark.ml.feature import NGram
from pyspark.ml.feature import Tokenizer

import boto3

# create spark session if one doesn’t exist already
spark = SparkSession.builder.getOrCreate()

# s3 = boto3.client('s3')
# s3.download_file('blossom-data-engs', 'data-scientist-job-market-in-the-us.zip', 'data-scientist-job-market-in-the-us.zip')
# s3.download_file('blossom-data-engs', 'all-us-stocks-tickers-company-info-logos.zip', 'all-us-stocks-tickers-company-info-logos.zip')
#

#load data science dataset
all_data = spark.read.csv(
            "alldata.csv",
            header=True, inferSchema=True, escape='"', multiLine=True)

#rename description column
all_data = all_data.selectExpr("description as describe", 'position', 'company', 'reviews', 'location')

#filter all null values in data science dataset
all_data = all_data.filter(all_data.position.isNotNull())
all_data = all_data.filter(all_data.location.isNotNull())

#load companies dataset
companies = spark.read.csv(
            "companies.csv",
            header=True, inferSchema=True, escape='"', multiLine=True)

#filter all null values in company dataset
companies = companies.filter(companies.description.isNotNull())
companies = companies.filter(companies.industry.isNotNull())

#join the two datasets
joined_df = companies.join(all_data, companies['company name'] == all_data.company)
joined_df.show()

#generate tokenizer
tokenizer = Tokenizer(inputCol='position', outputCol='token')
all_data = tokenizer.transform(all_data)

#generate ngrams
ngram = NGram(n=2, inputCol="token", outputCol="ngrams")
all_data = ngram.transform(all_data)

#explode, split , group and count
all_data.select(['ngrams', 'location']).select('location', F.explode('ngrams').alias('ngrams'))
cities = all_data.select(['ngrams','location']).select(F.explode('ngrams').alias('ngrams'),F.split(all_data['location'], ',')[0].alias('city'))
cities.groupBy(['ngrams', 'city']).count().orderBy("count", ascending=False).show()

#generate tokenizer
tokenizer = Tokenizer(inputCol='description', outputCol='token')
companies = tokenizer.transform(companies)

#generate ngrams
ngram = NGram(n=2, inputCol="token", outputCol="ngrams")
companies = ngram.transform(companies)

#explode, split , group and count
new_companies = companies.select(['ngrams','industry']).select(F.explode('ngrams').alias('ngrams'),'industry')
new_companies.groupBy(['ngrams', 'industry']).count().orderBy("count", ascending=False).show()

