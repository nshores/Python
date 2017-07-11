import nest_thermostat
import influxdb

nest = nest_thermostat.Nest("nick@shoresmedia.com", "4118nick")
nest.login()
nest.get_status()

temp = nest.temp_out(nest.status["shared"][nest.serial]["current_temperature"])
mode = nest.status["shared"][nest.serial]["hvac_ac_state"]

target = nest.temp_out(nest.status["shared"][nest.serial]["target_temperature"])

if mode is True:
    # print("Mode is cool")
    finalmode = 1
else:
    # print("Mode is not cool")
    finalmode = 0

from influxdb import client as influxdb

db = influxdb.InfluxDBClient("localhost", 8086, "", "", "cacti2")

data = [
    {
        "tags": {
            "host": "nest",
        },
        "measurement": "temp",
        "fields": {
            "Float_value": temp,
            "mode2": finalmode,
            "target": target
        }
    }
]
db.write_points(data)
