# coding=utf-8

import paho.mqtt.client as mqtt
import json

def client_mqtt(file):
    # Use a breakpoint in the code line below to debug your script
    client = mqtt.Client()
    client.connect("10.8.128.250", 1883)

    with open(file) as json_file:
        data = json.load(json_file)
        print('sending the mqtt request...')
        client.publish("esiea_grp7", json.dumps(data))
        print('json sended')

    client.disconnect()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client_mqtt("../data/json_test.json")
