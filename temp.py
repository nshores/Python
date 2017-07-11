#Define Sensor
sensor = W1ThermSensor()
#Grag Current Temp in F
temp = sensor.get_temperature(W1ThermSensor.DEGREES_F)

#Define influxdb stuff
host='192.168.99.118'
port='8086'
dbname = 'cacti2'
query = 'select value from cpu_load_short;'

client = InfluxDBClient(host=host, port=port, database=dbname)

json_body = [
        {
            "tags": {
                "host": "pi_probe",
            },            
            "measurement": "server_room_temp",
            "fields": {
                "Float_value": temp,
            }
        }
    ]


print("Write points: {0}".format(json_body))
client.write_points(json_body)

print("Queying data: " + query)
result = client.query(query)
