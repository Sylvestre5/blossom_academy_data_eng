<h1>Blossom Academy Fall 2019 Cohort - Data Engineering</h1>
# Project Title

Basic ETL pipeline to read data from a source, transform this data, then load the output into a prescribed location

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
- Anaconda 
- Amazon Simple Storage Service(S3)
- Boto3 client
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Anaconda -  https://www.anaconda.com/distribution/ (Python 3.7 version)
Amazon Simple Storage Service(S3) - https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
Boto3 - pip install boto3

```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### Tasks Performed

- Setup a working environment on computer to use throughout the program.
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

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
<div align="center">
  <h1>Blossom Academy Fall 2019 Cohort - Data Engineering</h1>
</div>

	
	
<h2>Project Two</h2>
I built a basic ETL pipeline to read data from a source, transform this data, 
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
    <p>d. Write out the output(from point c.) in the following formats;</p>
          <p> - Parquet</p>
          <p> - JSON (compressed using gzip)</p>
          <p> - AVRO</p>
- Upload the resulting 3 file to your S3 buckets blossom-data-eng-[student-name].
- Commit your code to your github repository.

