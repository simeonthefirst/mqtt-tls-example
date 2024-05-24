import paho.mqtt.client as mqtt
import ssl

# Define the MQTT broker details
broker = "localhost"
port = 8883
topic = "test/topic"

# Define the paths to the CA certificate and client certificate/key
ca_cert = "./ca.crt"
client_cert = "./client.crt"
client_key = "./client.key"

# Define the on_connect callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to the topic
    client.subscribe(topic)

# Define the on_message callback
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# Create an MQTT client instance
client = mqtt.Client(client_id="testclient", protocol=mqtt.MQTTv311)

# Set the TLS parameters
client.tls_set(ca_certs=ca_cert,
               certfile=client_cert,
               keyfile=client_key,
               cert_reqs=ssl.CERT_REQUIRED,
               tls_version=ssl.PROTOCOL_TLS,
               ciphers=None)

# Optional: Disable certificate hostname checking (not recommended for production)
#client.tls_insecure_set(True)

# Set the username and password if required by the broker
client.username_pw_set("username", "password")

# Assign the callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker, port, 60)

# Start the MQTT client
client.loop_forever()
