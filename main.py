from lastfm import *
from spotify import *
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get('/')
def read_root():
    return {'Funcionando': 'Sim'}

@app.get('/spotify-access-token')
def read_token():
    return getAccessToken()

@app.get('/spotify-now-playing')
def now_playing():
    response = requests.get(url=currentlyplaying, 
                            headers={'Authorization': 'Bearer ' + refreshao})
    if response.status_code == 204:
        return {'mensagem': 'Nada tocando no momento :p'}
    response = response.json()
    return {'title': {response["item"]["name"]}, 'artist': {response["item"]["artists"][0]["name"]}}

@app.get('/spotify-refresh-token')
def refresh_token():
    return getRefresh()

@app.get('/search/{search}')
def search(search: str):
    return spotifySearch(search)

@app.get('/lastfm-top-tracks')
def top_tracks():
    return getTopTracks()

@app.get('/lastfm-top-albums')
def top_albums():
    return getTopAlbums()

@app.get('/lastfm-top-artists')
def top_artists():
    return getTopArtists()

@app.get('/lastfm-recent-tracks')
def recent_tracks():
    return getRecentTracks()