import requests

try:
    api="http://127.0.0.1:5050"
    data=""
    result=requests.post(api,data=data)

    print(result)
    print(result.status_code)

except:
    print("error")
    print(result.status_code)

