from lastfm import *
from spotify import *
from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique, por exemplo, ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Funcionando': 'Sim'}

@app.get('/spotify-access-token')
def read_token():
    return getAccessToken()

@app.get('/spotify-now-playing')
def now_playing():
    return getNowPlaying()

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