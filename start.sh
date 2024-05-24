sudo apt-get update
sudo apt-get install openssl

./gen_keys.sh

mosquitto_passwd -c ./passwd username

mosquitto -c ./mosquitto.conf

pip3 install paho-mqtt
python3  client.py 