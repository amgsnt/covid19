#!/usr/bin/python

import requests
from datetime import datetime

def downloadData():

    url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/csv"

    print("Starting...{}".format(datetime.now()))

    s = requests.Session()
    r = s.get(url)

    file = open("covid19.csv", "w")
    file.write(r.text)
    file.close()
        
    print("Finish...{}".format(datetime.now()))
    
downloadData()
