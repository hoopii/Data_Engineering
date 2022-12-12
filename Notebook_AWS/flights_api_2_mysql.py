import pandas as pd
from datetime import datetime, date, timedelta
import requests
from sqlalchemy import create_engine
from pytz import timezone

def tomorrows_flight_arrivals(icao_list):

  today = datetime.now().astimezone(timezone('Europe/Berlin')).date()
  tomorrow = (today + timedelta(days=1))

  list_for_df = []

  for icao in icao_list:
    times = [["08:00","09:00"],["09:00","12:00"]]

    for time in times:
      url = f"https://aerodatabox.p.rapidapi.com/flights/airports/icao/{icao}/{tomorrow}T{time[0]}/{tomorrow}T{time[1]}"
      querystring = {"withLeg":"true","direction":"Arrival","withCancelled":"false","withCodeshared":"true","withCargo":"false","withPrivate":"false"}
      headers = {
          'x-rapidapi-host': "aerodatabox.p.rapidapi.com",
          'x-rapidapi-key': "put your key here"
          }
      response = requests.request("GET", url, headers=headers, params=querystring)
      flights_json = response.json()

      for flight in flights_json['arrivals']:
        flights_dict = {}
        flights_dict['arrival_icao'] = icao
        flights_dict['arrival_time_local'] = flight['arrival'].get('scheduledTimeLocal', None)
        flights_dict['arrival_terminal'] = flight['arrival'].get('terminal', None)
        flights_dict['departure_city'] = flight['departure']['airport'].get('name', None)
        flights_dict['departure_icao'] = flight['departure']['airport'].get('icao', None)
        flights_dict['departure_time_local'] = flight['departure'].get('scheduledTimeLocal', None)
        flights_dict['airline'] = flight['airline'].get('name', None)
        flights_dict['flight_number'] = flight.get('number', None)
        flights_dict['data_retrieved_on'] = datetime.now().astimezone(timezone('Europe/Berlin')).date()
        list_for_df.append(flights_dict)

  return pd.DataFrame(list_for_df)

def flights_api_2_mysql():
    
    icaos = ['EDDL', 'EGLL']
    
    df = tomorrows_flight_arrivals(icaos)
    
    database = 'collected_data'

    username = 'root'

    password = 'put your password here'

    host = 'wbs-project3-db.ccyhe0gcjtam.eu-central-1.rds.amazonaws.com'

    sqlEngine       = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}', pool_recycle=3600)

    dbConnection    = sqlEngine.connect()

    tableName = 'flights_airports_1'

    try:

        frame = df.to_sql(tableName, dbConnection, if_exists='append', index = False);

    except ValueError as vx:

        print(vx)

    except Exception as ex:   

        print(ex)

    else:

        print("The data was pushed sucessfully to Table %s."%tableName);   

    finally:

        dbConnection.close()
        
def lambda_handler(event, context):
    flights_api_2_mysql()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }