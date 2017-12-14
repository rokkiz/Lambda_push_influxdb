from __future__ import print_function
import requests
import json
import base64

def lambda_handler(event,context):
    for record in event['Records']:
        #Kinesis data is base64 encoded so decode here
        message = json.loads(base64.b64decode(record['kinesis']['data']))
        print("Decoded payload: " + str(message))
        #print("device_id " + str(message['device_id']))
        url = "http://52.76.29.185:80/write"
        querystring = {"db":"sensor_data"}
        payload = "sensor,device_id=%s,sensor_type=%d,data_type=%d,timestamp_gw=%d,espPkgNum=%d,espTS=%d data=%f" % (message['device_id'],int(message['sensor_type']),int(message['data_type']),int(message['timestamp']),int(message['espPkgNum']),int(message['espTS']),message['data'])
        response = requests.request("POST", url, data=payload, params=querystring)
        print(response.text)
        print(payload)
    return 'done'
