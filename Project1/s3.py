import pandas as pd
import boto3


#load dataset
df = pd.read_csv('free-7-million-company-dataset.zip', compression='zip')

#filter out companies without domain
df.dropna(subset=['domain'], inplace=True)


#save dataset to JSON format
df.to_json("free-7-million-company-dataset-json.gzip", orient='records', compression='gzip')

#save dataset to parquet format
df.to_parquet("free-7-million-company-dataset.parquet", compression='gzip')

#initiate s3 bucket client
s3 = boto3.client('s3')

#upload JSON dataset to s3
s3.upload_file('free-7-million-company-dataset-json.gzip', 'blossom-data-eng-priscilla', 'free-7-million-company-dataset-json.gzip')

#upload Parquet dataset to s3
s3.upload_file('free-7-million-company-dataset.parquet', 'blossom-data-eng-priscilla', 'free-7-million-company-dataset.parquet')
