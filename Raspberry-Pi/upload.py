import requests, time

def uploadinfo(plate, status): 
    url = 'http://192.168.1.94:1880/iot'
    headers = {
        'Content-type':'text/json'
        }

    t = round(time.time());
    try:
        r = requests.post(url,
                      headers=headers,
                      json =  {"plate":plate, "time": t, "status":status},
                      timeout = 3
                      )
    except:
        return