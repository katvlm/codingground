import http.client

conn = http.client.HTTPSConnection("apip.oracleau.cloud")

headers = {
    'x-app-key': "6386e63a-f782-4c9e-9649-c34544aa4876",
    'cache-control': "no-cache",
    }
    
conn.request("GET", "/api/medrec/physicians", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))