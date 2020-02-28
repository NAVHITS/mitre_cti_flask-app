import requests
import base64
# en = base64.b64encode('kruptos.club')

parameters = {
  "ioc": "dGVwZmVyLm1x",
  "probe": "1",
  "pretty": "1",
  "key": "c666f37d3dad136f44b28d4a97450d7fc1b52d5ca20ee46662568e4578e4f80d"
}

r = requests.get('https://pulsedive.com/api/analyze.php', params=parameters) 

t = r.json()
print(t)