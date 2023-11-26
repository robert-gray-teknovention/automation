import paho.mqtt.client as mqtt
import ssl


class MqttConnection():

    def __init__(self, server):
        self.server = server

    def connect(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(self.server.username, self.server.password)
        self.client.tls_set(certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED)
        self.client.connect(
            host=self.server.host,
            port=self.server.port,
            keepalive=60
        )
        print(str(self.server))
        print("We just tried connecting!!")
        self.client.loop_forever()

    def on_connect(self, mqtt_client, userdata, flags, rc):
        if rc == 0:
            print('Connected successfully')
            mqtt_client.subscribe('test')
        else:
            print('Bad connection. Code:', rc)

    def on_message(self, mqtt_client, userdata, msg):
        print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
