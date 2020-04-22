import datetime, random

def get_deviceId():
    list_of_devices = ["354232234", "234234342", "134234112", "434234123", "534234124", "234235423"]
    return random.choice(list_of_devices)

def get_temperature():
    return random.randrange(-5, 40, 1)

def get_location():
    return random.uniform(-180,180), random.uniform(-90, 90)

def get_time():
    return str(datetime.datetime.utcnow())