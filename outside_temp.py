import forecastio

api_key = '08ac8a31862a6eae179446a47d198146'
lat = 38.533463
lng = -121.439237 

forecast = forecastio.load_forecast(api_key, lat, lng)

temp = forecast.currently().temperature



from influxdb import client as influxdb

db = influxdb.InfluxDBClient("localhost", 8086, "", "", "cacti2")

data = [
        {
            "tags": {
                "host": "forecastio",
            },            
            "measurement": "outsidetemp",
            "fields": {
                "outside_temp": temp
            }
        }
    ]
db.write_points(data)
