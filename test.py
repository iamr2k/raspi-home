import requests
url = "http://raspberrypi.local/api/"
data = {
    "temp":12.4
}
requests.post(url, data=data)