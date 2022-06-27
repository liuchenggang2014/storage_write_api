from flask import Flask
from google.auth import crypt
from google.auth import jwt
import time
import os
import io
import json
import base64
import requests

# Service account key path from ADC
# credential_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# sa_keyfile = './cliu201-pubsub.json'


# Audience 
# audience="https://pubsub.googleapis.com/google.pubsub.v1.Publisher"
# audience="https://pubsub.googleapis.com"

# Get service account email and load the json data from the service account key file. 
# with io.open(sa_keyfile, "r", encoding="utf-8") as json_file:
#     data = json.loads(json_file.read())
#     sa_email=data['client_email']

# Generate the Json Web Token from sa json file
# def generate_jwt(sa_keyfile,
#                  sa_email,
#                  audience,
#                  expiry_length=3600):

#     """Generates a signed JSON Web Token using a Google API Service Account."""

#     now = int(time.time())

#     # build payload
#     payload = {
#         'iat': now,
#         # expires after 'expiry_length' seconds.
#         "exp": now + expiry_length,
#         # iss must match 'issuer' in the security configuration in your
#         # swagger spec (e.g. service account email). It can be any string.
#         'iss': sa_email,
#         # aud must be either your Endpoints service name, or match the value
#         # specified as the 'x-google-audience' in the OpenAPI document.
#         'aud':  audience,
#         # sub and email should match the service account's email address
#         'sub': sa_email,
#         'email': sa_email
#     }

#     # sign with keyfile
#     signer = crypt.RSASigner.from_service_account_file(sa_keyfile)
#     jwt_token = jwt.encode(signer, payload)
#     #print(jwt_token.decode('utf-8'))
#     return jwt_token.decode('utf-8')

# https://cloud.google.com/run/docs/securing/service-identity#access_tokens
# generate access tokey by cloudrun's metadata 
def generateAccessToken():
    # Request Headers
    headers = {
        'Metadata-Flavor': 'Google'
    }

    url = 'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token?scopes=https://www.googleapis.com/auth/pubsub'

    # Get response data
    response = requests.get(url, headers=headers)
    print(response.text)
    return response.text

app = Flask(__name__)
@app.route('/hello', methods=['GET', 'POST'])
def welcome():
    return "Hello World!\n"

@app.route('/', methods=['GET', 'POST'])
def hello():
    return 'Welcome to My Watchlist11111!\n'

@app.route('/api', methods=['GET'])
def api():
    # return generate_jwt(sa_keyfile, sa_email, audience)
    return generateAccessToken()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)



