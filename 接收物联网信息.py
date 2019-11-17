import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("deviceName/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("fggse33/gdwrobot", "tJXurvdVGB9bDBDI")
client.connect("fggse33.mqtt.iot.gz.baidubce.com", 1883, 60)

client.loop_forever()