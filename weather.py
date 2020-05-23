import requests
import os
import json

def getweather(city="bangalore"):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metrics&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    info=os.popen('curl ipinfo.io').read()
    info=json.loads(info)
    city=info["city"]
    try:
        r = requests.get(url.format(city)).json()
        temp=str(r['main']['temp'])
        des=str(r['weather'][0]['description'])
        weather = "Currently in "+city+" Its "+temp+" degree and "+des+" ."
        return weather
    except:
        weather="I cannot do that at a moment"
