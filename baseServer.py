# -*- coding: utf-8 -*-

from flask import Flask, request, abort, Response
# from urllib.parse import parse_qs, urlparse
import requests
import json
import avayasms
import getflights
import pourv0
import dashaHVAC

app = Flask(__name__)

import json


def sendMedia(url2):
    url = " http://b941-35-204-206-186.ngrok.io/visitor"

    payload = json.dumps({
    "img": url2
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


@app.route('/getsms', methods=['POST','GET'])
def webhook():
    if request.method == 'GET':
        print("************************************")
        print("Response:",request.args['Body'])
        print("From:",request.args['From'])
        print("---------------------------------------")

        body = request.args['Body'].lower()     
        if 'code' in body:
            if '7174' in body:
                ## true
                print ('verified')
                txt = "hey there human. thanks for using dashArm and dashCam"
                avayasms.sendSms(request.args['From'], txt)
        return '', 200
    else:
        abort(400)



@app.route('/mms', methods=['POST','GET'])
def mms():
    if request.method == 'POST':
        print("************************************")
        print("Response",request.form['MediaUrl'])
        sendMedia(request.form['MediaUrl'])
        print("---------------------------------------")
        return '', 200
    else:
        abort(400)




@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # js = transcribe()
    
    js = {}
    js['status'] = 'done'


    resp = Response(js, status=200, mimetype='application/json')

    print ("****************************")
    print (resp)

    return js
    # return resp


@app.route("/getreturn", methods=['GET', 'POST'])
def getreturn():

    res = request.get_json()
    print (res)

    resraw = request.get_data()
    print (resraw)
    
    orig = res['origin']
    dest = res['destination']
    dt = res['date']
    rt = res['return']
    
    jd, lusd = getflights.getcheapestreturn(dt, orig, dest, rt)

##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()



    status = {}
    status["server"] = "up"
    status["request"] = res 
    status['cheapest'] = str(lusd)
    status['flight'] = str(jd)

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp


@app.route("/getoneway", methods=['GET', 'POST'])
def getoneway():

    res = request.get_json()
    print (res)

    resraw = request.get_data()
    print (resraw)
    
    orig = res['origin']
    dest = res['destination']
    dt = res['date']
    
    jd, lusd = getflights.getcheapestoneway(dt, orig, dest)

##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()



    status = {}
    status["server"] = "up"
    status["request"] = res 
    status['cheapest'] = str(lusd)
    status['flight'] = str(jd)

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp




@app.route("/getHVAC", methods=['GET', 'POST'])
def getHVAC():

    res = request.get_json()
    print (res)

    resraw = request.get_data()
    print (resraw)
    
    mesg = "Dasha says " +res['message']
    
    pourv0.pispeak(mesg)
    
    pd = dashaHVAC.getreadings(1)
    
    
    
##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()



    status = {}
    status["server"] = "up"
    status["request"] = res 
    status['data'] = pd
    # status['flight'] = str(jd)

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp




@app.route("/gettodos", methods=['GET', 'POST'])
def gettodos():

    res = request.get_json()
    print (res)

    resraw = request.get_data()
    print (resraw)
    
    # orig = res['origin']
    dest = res['destination']
    # dt = res['date']
    
    lat, lon = getflights.getcoords(dest)
    
    print(lat, lon)
    
    acts = getflights.getactivities(lat, lon, 18)
    # pois = getflights.getpois(lat, lon, 18)
    
    # summ, risk = getflights.getcovid(dest)
    
    # jd, lusd = getflights.getcheapestoneway(dt, orig, dest)

##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()



    status = {}
    status["server"] = "up"
    status["request"] = res 
    status['activities'] = acts
    # status['points of interest'] = pois

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp



@app.route("/makebeverage", methods=['GET', 'POST'])
def makebeverage():

    res = request.get_json()
    print (res)

    resraw = request.get_data()
    print (resraw)
    
    # orig = res['origin']
    dtype = res['drinktype']
    # dt = res['date']
    
    # summ, risk = getflights.getcovid(dest)
    
    # jd, lusd = getflights.getcheapestoneway(dt, orig, dest)
    
    
    ingstat = pourv0.testpour(dtype) 
##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()



    status = {}
    status["server"] = "up"
    status["request"] = res 
    status['drinktype'] = dtype
    status['ingredients'] = ingstat

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp



@app.route("/atmydoor", methods=['GET', 'POST'])
def atmydoor():

    res = request.get_json()
    print (res)

    resraw = request.get_data()
    print (resraw)
    
    # orig = res['origin']
    mesg = res['message']
    # dt = res['date']
    pourv0.pispeak(mesg)
    
    ## os.system('python .\baseimagegrabber.py')
    ## os.system('python .\gcpuploader.py dashaDoor.jpg hackybucket')
    
    avayasms.sendSms('15714901702', 'hello from dashaCam. here is a picture outside your front door at the moment. https://storage.googleapis.com/hackybucket/dashaDoor.jpg  Your message has been relayed to the front door. Thank you!')
    # summ, risk = getflights.getcovid(dest)
    
    # jd, lusd = getflights.getcheapestoneway(dt, orig, dest)
    
    
    # ingstat = pourv0.testpour(dtype) 
##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()



    status = {}
    status["server"] = "up"
    status["request"] = res 
    status['message'] = mesg
    # status['ingredients'] = ingstat

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp




@app.route("/getcovidrisk", methods=['GET', 'POST'])
def getcovidrisk():

    res = request.get_json()
    print (res)

    resraw = request.get_data()
    print (resraw)
    
    # orig = res['origin']
    dest = res['destination']
    # dt = res['date']
    
    summ, risk = getflights.getcovid(dest)
    
    # jd, lusd = getflights.getcheapestoneway(dt, orig, dest)

##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()



    status = {}
    status["server"] = "up"
    status["request"] = res 
    status['risk'] = risk
    status['summary'] = summ

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp



@app.route("/dummyJson", methods=['GET', 'POST'])
def dummyJson():

    res = request.get_json()
    print (res)

    resraw = request.get_data()
    print (resraw)

##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()


    status = {}
    status["server"] = "up"
    status["request"] = res 

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp


if __name__ == '__main__':
    # app.run()
    app.run(debug=True, host = 'localhost', port = 8005)
