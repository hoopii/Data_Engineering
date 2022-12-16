# Data Engineering Skills for Data Scientists
### Basic Data Engineering Skills for Data Scientists: Data Collection and Pipelines

![](picture_project.png)

## Use Case
The (fictional) businnes use case is the following: Hired as a data engineer for an upcoming start up e-scooter sharing company that rents scooters in different european cities, I was asked to supply them with some data that better helps predicting e-scooter movement.

Ideally, scooters get rearranged organically by having certain users moving from point A to point B, and then an even number of users moving from point B to point A. However, some elements create asymmetries, for example weather and arrivals of tourists in the city:
- On rainy and cold days e-scooter usage decreases drastically.
- Whenever planes with backpack young tourists land, a lot of scooters are needed close to the airport.

So a good way to start is collecting data on weather forecasts and future flight arrivals at city airports. To supply the e-scooter-sharing company with basic data to anticipate scooter movement using Python we will gather data on weather and future flight arrivals using API's. We support those informations by scraping wikipedia for demographical data on the cities

## Goal 
I gathered data from the web using APIs and webscraping techniques, stored it in a database on the cloud with AWS services and automated this process as part of my Data Science Bootcamp at WBS CODING SCHOOL. Here’s how I put together the API requests, parsed the JSON response and put the data into a nice looking dataframe.

    In many cases Data Scientists or Data Analysts don’t have access to preprocessed, well structured, cleaned up data ready to use.  
    More often and particularly in small start-ups and companies, employers expect data scientists to have some very basic data engineering skills,  
    to take care of obtaining data themselves, performing ETL operations and setting up databases in the cloud. 

## Skills/Tools
- *Collect data from the internet by writing a web scraping script using Python’s library [beautifulsoup](https://beautiful-soup-4.readthedocs.io/en/latest/).*   
- *Collect data from the internet through APIs, assembling the call directly with the [requests library](https://pypi.org/project/requests/).*   
- *Write for loops and list comprehensions on Python to perform tasks iteratively.*
- *Do JSON Parsing.*   
- *[Connect Python with MySQL using SQLAlchemy](https://www.sqlalchemy.org/).*  
- *Set up an RDS instance on AWS and enable the connection between your computer and the cloud instance, both through a standard client such as MySQL Workbench and through Python, by using MySQL-python-connector.*   
- *Populate your MySQL tables with collected data through INSERT queries executed from a Python script.*  
- *Use AWS:Lambda functions to run the code in the cloud and schedule the Lambda functions to run on a specified schedule.*   
- *Populate your MySQL tables with collected data through INSERT queries executed from a Python script.*   
- *Set up Lambda functions to run your code in the cloud (using a serverless service).*   
- *Create custom Layers with ad-hoc dependencies for the Lambda functions.*   
- *Schedule Lambda functions to run on a specified schedule.*   

## Basic Steps in this Project: 

![grafik](https://user-images.githubusercontent.com/100354393/206842323-8d05a438-ba00-4afd-b1b4-ff32f1f15b40.png)

We will first build the pipeline locally and, only once it’s done, we will move to the cloud: we anticipate we will make mistakes, identify needs we were not foreseeing and come up with new ideas along the way. We want all of this to happen as early as possible and in a context where debugging code or altering the design of a database is still easy.

Phase 1: Create a Local Pipeline: 
- Scrape data from the web
- Collect data with APIs
- Store data on a local MySQL instance

Phase 2: Set up Pipeline in the Cloud: 
- Set up a cloud database
- Move scripts to Lambda
- Automate the pipeline 

The deliverable of this project is a written Medium article of what you have accomplished: 
- [Medium Article on Data Collection process with API's](https://medium.com/@rene.markovits/data-engineering-skills-for-data-scientists-c095e01dd82b): The article guides and explains the code I used to collect the data using API's

## Limitations: 
It’s important to limit the scope of this project: We create a very basic pipeline in the cloud. 
All tech projects start with a simple approach before moving on to more complicated solutions.
- We will not connect our data pipeline to a BI tool. 
- We will not be creating either a data warehouse or a data lake.
- We will not work with big data, data streaming or parallel computing.

## Files in this repository: 
- Folder for notebooks on APIs:  
  - [Gather data on future flight arrivals](../main/Notebooks_APIs/flights_arrivals_API_to_dataframe.ipynb)  
  - [Gather data on future weather](../main/Notebooks_APIs/weather_API_to_dataframe.ipynb)   
- Folder for notebook on webscraping:   
  - [Scrape Wikipedia for basic information about the cities](../main/Notebooks_Webscraping/extract_wiki.ipynb)  
- [Create empty tables in SQL before pushing the data](../main/Prepare_Tables_in_SQL.sql)  
- Folder for notebooks on pushing data to local database/mySQL  
  - [push basic information about the cities to mySQL](../main/Notebooks_Push_Data_Local_Database/Wiki_scraper_mysql.ipynb)
  - [push data on flight arrivals to mySQL](../main/Notebooks_Push_Data_Local_Database/flights_data_to_mysql.ipynb)
  - [push data on weather to mySQL](../main/Notebooks_Push_Data_Local_Database/weather_API_to_mysql.ipynb)
- Folder for connecting lambda function:  
  - [Connect lambda function to RDS instance](/Notebook_AWS/flights_api_2_mysql.py)
