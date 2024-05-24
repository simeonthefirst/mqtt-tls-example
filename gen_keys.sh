# CA
openssl ecparam -genkey -name prime256v1 -out ca.key
openssl req -new -x509 -key ca.key -out ca.crt -days 365 -subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=CA"

# Server
openssl ecparam -genkey -name prime256v1 -out server.key
openssl req -new -key server.key -out server.csr -subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=localhost"
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365

# Client
openssl ecparam -genkey -name prime256v1 -out client.key
openssl req -new -key client.key -out client.csr -subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=localhost"
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
