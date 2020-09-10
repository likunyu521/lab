import requests

url = "https://www.v2ex.com/api/topics/hot.json"

payload = {}
headers = {
  'Cookie': '__cfduid=daa18b0d1f03341a78fffa1399e5c63fb1597983188'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
