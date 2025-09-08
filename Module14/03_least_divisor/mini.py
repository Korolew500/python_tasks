import http.client

conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")

payload = "{\"messages\":[{\"role\":\"user\",\"content\":\"hi\"}],\"web_access\":false}"

headers = {
    'x-rapidapi-key': "b478d3c0c1msh838b773334c80ecp1ff63ajsn8217b0601058",
    'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/gpt4", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
