import datetime

def date():
    today = str(datetime.date.today())
    day ="Today's date is "+ today
    return day

def time():
    today = datetime.datetime.now()
    hour = str(today.hour)
    minutes = str(today.minute)
    time = "Now its " + hour + " hour" + minutes + " minutes"
    return time
