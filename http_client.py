import requests 
data={
    "X":[[1,2,3]]
}
port=8000
url=f"http://localhost:{port}/predict_wx"
response=requests.post(url,json=data)
result=response.json()
print(result)