
from amadeus import Client, ResponseError
import json
from dateutil.parser import parse
import amadeustokengrabber
import requests


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


amadeus = Client(
    client_id='iXqeIZDXSAeG7aKGAG5PErEXxxNJWNiT',
    client_secret='182VSOEZv6khP4aj'
)


def getcoords(loc):
    url = "http://api.positionstack.com/v1/forward?access_key=9f55832839eb43789ecf31ecfc1846cc&query=" + loc

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    js = json.loads(response.text)
    
    print (type(js['data']))
    lat = js['data'][0]['latitude']
    lon = js['data'][0]['longitude']
    
    print (lat, lon)
    
    return lat, lon



def getpois(lat, lng, rad):
    try:
        '''
        What are the popular places (based on a geo location and a radius)
        '''
        
        
        response = amadeus.reference_data.locations.points_of_interest.get(latitude=lat, longitude=lng)
        print(response.data)
        
        
        acts = []
        
        for d in response.data:
            print (d['name'], d['category'])
            
            acts.append(d['name'] + " - " + d['category'])
        
        return acts
        
        
    except ResponseError as error:
        raise 


def getactivities(lat, lng, rad):
    try:
        '''
        Returns activities for a location  based on geolocation coordinates
        '''
        
        # lat = 40.41436995
        # lng = -3.69170868
        
        response = amadeus.shopping.activities.get(latitude=lat, longitude=lng, radius="18")
        print(response.data)
        
        # js = json.loads(response.data)
        
        acts = []
        
        for d in response.data:
            print (d['name'])
            acts.append(d['name'])
        
        return acts
        
        
        
    except ResponseError as error:
        raise error



def getcovid(city):
    
    city = city.lower()
    
    if 'chi' in city:
        city = 'CHI'
    
    if 'new' in city:
        city = 'NYC'
    
    if 'mia' in city:
        city = 'MIA'
    
    if 'los' in city:
        city = 'LAX'
    
    if 'las' in city:
        city = 'LAS'
    
    if 'tor' in city:
        city = 'YYZ'

    url = "https://test.api.amadeus.com/v1/duty-of-care/diseases/covid19-area-report?countryCode=US&cityCode=" + city

    print(url)
    
    token = 'Bearer ' + amadeustokengrabber.gettoken()

    payload={}
    headers = {
    'Authorization': token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    
    js = response.json()
    
    # print(js)
    
    # print (js['data']['subAreas'][0]['summary'])
    # print (js['data']['subAreas'][0]['diseaseRiskLevel'])
    
    summ = js['data']['subAreas'][0]['summary']
    risk = js['data']['subAreas'][0]['diseaseRiskLevel']
    
    summ = summ.replace('<p>', '')
    summ = summ.replace('</p>', '')
    # summ = summ.replace('\"', '')
    # summ = summ.replace('"\', '')
                        
    print (summ, risk)
    
    return summ, risk
    






def getcheapestoneway(dat, orig, dest):
    
    orig = orig.lower()
    # dat = dat.lower()
    dest = dest.lower()
    
    ##code for subset of IATA codes
    
    if 'chi' in orig:
        orig = 'CHI'
    
    if 'new' in orig:
        orig = 'NYC'
    
    if 'mia' in orig:
        orig = 'MIA'
    
    if 'los' in orig:
        orig = 'LAX'
    
    if 'las' in orig:
        orig = 'LAS'
    
    if 'tor' in orig:
        orig = 'YYZ'
    
    if 'chi' in dest:
        dest = 'CHI'
    
    if 'new' in dest:
        dest = 'NYC'
    
    if 'mia' in dest:
        dest = 'MIA'
    
    if 'los' in dest:
        dest = 'LAX'
    
    if 'las' in dest:
        dest = 'LAS'
    
    if 'tor' in dest:
        dest = 'YYZ'    
    
    
    datetime = parse(dat)
    
    print(str(datetime.date()))
    
    dat = str(datetime.date())
    print (orig, dat, dest)
    
    try:
        '''
        Find the cheapest flights from origin to destination
        '''
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=orig, destinationLocationCode=dest, departureDate=dat, adults=1)
        # print(response.data)
        
        print (type(response.data))
        
        lowest = 1000000.00
        jd = {}
        for d in response.data:
            # print (d)
            # print (d['price']['grandTotal'])
            if float(d['price']['grandTotal']) < lowest:
                lowest = float(d['price']['grandTotal'])
                jd = d
        
        lusd = round(lowest * 1.12, 2)
        print (jd)
        print (lusd)
        
        return jd, lusd
    
            
            

    except ResponseError as error:
        raise error


def getcheapestreturn(dat, orig, dest, ret):
    
    orig = orig.lower()
    # dat = dat.lower()
    dest = dest.lower()
    
    ##code for subset of IATA codes
    
    if 'chi' in orig:
        orig = 'CHI'
    
    if 'new' in orig:
        orig = 'NYC'
    
    if 'mia' in orig:
        orig = 'MIA'
    
    if 'los' in orig:
        orig = 'LAX'
    
    if 'las' in orig:
        orig = 'LAS'
    
    if 'tor' in orig:
        orig = 'YYZ'
    
    if 'chi' in dest:
        dest = 'CHI'
    
    if 'new' in dest:
        dest = 'NYC'
    
    if 'mia' in dest:
        dest = 'MIA'
    
    if 'los' in dest:
        dest = 'LAX'
    
    if 'las' in dest:
        dest = 'LAS'
    
    if 'tor' in dest:
        dest = 'YYZ'    
    
    
    datetime = parse(dat)
    
    print(str(datetime.date()))
    
    dat = str(datetime.date())
    
    datetime = parse(ret)
    
    print(str(datetime.date()))
    
    ret = str(datetime.date())
    
    print (orig, dat, dest, ret)
    
    try:
        '''
        Find the cheapest flights from origin to destination
        '''
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=orig, destinationLocationCode=dest, departureDate=dat, returnDate = ret, adults=1)
        # print(response.data)
        
        print (type(response.data))
        
        lowest = 1000000.00
        jd = {}
        for d in response.data:
            # print (d)
            # print (d['price']['grandTotal'])
            if float(d['price']['grandTotal']) < lowest:
                lowest = float(d['price']['grandTotal'])
                jd = d
        
        lusd = round(lowest * 1.12, 2)
        print (jd)
        print (lusd)
        
        return jd, lusd
    
            
            

    except ResponseError as error:
        raise error




##testing

# getcheapestoneway("20th December 2021", "New York", "Miami")

# getcovid("new york")

# getcoords("new york")

# getactivities(40.41436995, -3.69170868, 18)

# getpois(40.41436995, -3.69170868, 18)

# getcheapestreturn("20th December 2021", "New York", "Miami", "29th December 2021")