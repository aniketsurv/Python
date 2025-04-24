#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:41:13 2020

@author: Soniya Paradkar
"""
import json
import os
import paho.mqtt.client as paho

def get_request():
    request_obj = {
        "CallerInfo":{
                        "source":["Android_ClouzerEdgeInstaller","soulHub"],  
                        "caller":"activity_name_button_click",
                        # "portalAction" : False,
                    },
          "data":
            {
                "entity_type":"userlist",
                "and":
                {
                    "eq":
                    {
                        'userId': ''
                    }
                }
                
            },
                "communicationId":"1603353540019calculateRoomWiseAQI897"
        }

    return request_obj

#%%
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

broker = "192.168.4.5"
port = 8886
client= paho.Client("qb_test_delete")
client.username_pw_set(username="CEDPython",password="@$0uL|?yT#0n")
client.connect(broker,port)
client.on_connect = on_connect

request_obj = get_request()
client.publish("soulDb/delete",json.dumps(request_obj))
client.disconnect()
print("qb_test_delete : published request")