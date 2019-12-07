<div align="center">
   <h1>Blossom Academy Fall 2019 Cohort - Data Engineering</h1>
	
	
<h2>Project One</h2>
I built a btasic ETL pipeline to read data from a source, transform this data, 
then load the output into a prescribed location.

Tools Used
- Pandas 
- Amazon Simple Storage Service(S3)
- Jupyter Notebook
- Anaconda
- Boto3 client

<h2>Task Performed</h2>

- Setup a working environment on computer to use throughout the program.
- Write a python script with the following features; 
    <p>a. Download the 7+ Million Dataset from S3 [bucket: blossom-data-engs key:-project1/free-7-million-company-dataset.zip].</p>
    <p>b. Read the file with pandas.</p>
    <p>c. Filter out companies without a domain name using pandas.</p>
    <p>d. Write out the output(from point c.) in the following formats</p>
         - Parquet
         - JSON (compressed using gzip)
         - AVRO
- Upload the resulting 3 file to your S3 buckets blossom-data-eng-[student-name].
- Commit your code to your github repository.

</div>


