from fastapi import FastAPI
import requests
import base64
from dotenv import dotenv_values, load_dotenv
import os

load_dotenv()

clientid = os.getenv('clientid')
secretid = os.getenv('secretid')
refreshtoken = os.getenv('refreshtoken')
base64_auth = base64.b64encode(f"{clientid}:{secretid}".encode()).decode()

tokenendpoint = os.getenv('tokenendpoint')
currentlyplaying = os.getenv('currentlyplaying')

app = FastAPI()

def getAccessToken():
    response = requests.post(url=tokenendpoint, 
                            data={'grant_type': 'client_credentials'},
                            headers={'Authorization': 'Basic ' + base64_auth,
                                    'Content-Type': 'application/x-www-form-urlencoded'})
    response = response.json()
    return response

def getRefresh():
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refreshtoken
    }
    headers = {
        'Authorization': 'Basic ' + base64_auth,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(url=tokenendpoint, data=data, headers=headers)
    return response.json()


access_token = getAccessToken()['access_token']
refreshao = getRefresh()['access_token']