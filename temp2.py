import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
def check():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        url = "http://raspberrypi.local/api/"
        data = {
            "temp":temperature,
            "humidity":humidity
        }
        requests.post(url, data=data)
    return True