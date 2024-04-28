import requests
def make_request(requestbody, url, headers, method):
    if method == "POST":
        v = requests.post(url=url, json=requestbody, headers=headers)

        return v


    
if __name__ == "__main__":

    requestsbody ={
        "fullname" : "john",
        "nickname" : "johne",
        "age": 67
    }
    
    url = "http://127.0.0.1:8000/api/v1/programmers/"

    headers = {
         'Content-Type': 'application/json'

    }
    method = 'POST'
    ram_usage = make_request(requestsbody, url,headers, method )
    print(ram_usage)