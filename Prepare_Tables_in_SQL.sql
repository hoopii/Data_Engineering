CREATE DATABASE collected_data; 

Use collected_data; 

CREATE TABLE wiki_scrape (
	id INT AUTO_INCREMENT,
	city VARCHAR(20),
    country VARCHAR(20), 
    state VARCHAR(20), 
    pop_city_state VARCHAR(20), 
    pop_urban VARCHAR(20), 
    pop_metro VARCHAR(20), 
    PRIMARY KEY (id)
); 

SELECT * FROM wiki_scrape; 


CREATE TABLE weather_data (
	id INT , 
    city_id INT, 
    city VARCHAR (20), 
    forecast_time DATETIME, 
    outlook VARCHAR(20), 
    temperature FLOAT(10),
    temperature_feels_like FLOAT (10),
    wind_speed FLOAT (10),
    rain VARCHAR (20), 
    PRIMARY KEY (id)
); 	


CREATE TABLE flights_airports (
id INT AUTO_INCREMENT,
icao VARCHAR (20),  
name VARCHAR (80), 
iata VARCHAR (20),
municipalityName VARCHAR (20), 
location_lat FLOAT,
location_lon FLOAT,
Countrycode VARCHAR(10), 
information_retrieved_at VARCHAR(20),
PRIMARY KEY (id));

CREATE TABLE flights_arrivals (
id INT AUTO_INCREMENT,flights_airports
number_1 VARCHAR(40), 
callSign VARCHAR(40), 
status_1 VARCHAR(40), 
codeshareStatus VARCHAR(40), 
isCargo VARCHAR(40), 
departue_airiport_icao VARCHAR(40), 
departure_airport_iata VARCHAR(40), 
departure_airport_name VARCHAR(40), 
arrival_scheduledTimeLocal VARCHAR(40), 
arrival_actualTimeLocal VARCHAR(40), 
arrival_scheduledTimeUtc VARCHAR(40), 
arrival_actualTimeUtc VARCHAR(40), 
arrival_quality VARCHAR(40), 
aircraft_model VARCHAR(40), 
airline_name VARCHAR (40), 
information_retrieved_at VARCHAR (40),
icao VARCHAR (40),
PRIMARY KEY (id)
); 
 

-- INSERT INTO weather_data (city_id, forecast_time, outlook, temperature, temperature_feels_like, wind_speed, rain)
-- VALUES (1, 'tomorrow', 'goof', 7.3, 4.3, 100, "4.4");
SELECT * FROM flights_arrivals;
TRUNCATE TABLE weather_data_id; 

-- SELECT COLUMN_NAME, DATA_TYPE 
-- FROM INFORMATION_SCHEMA.COLUMNS 
-- WHERE TABLE_NAME = 'weather_data'



    
