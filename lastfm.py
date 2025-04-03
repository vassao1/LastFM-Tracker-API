from fastapi import FastAPI
import requests
from dotenv import dotenv_values, load_dotenv
import os

load_dotenv()

app = FastAPI()

lastfmapikey = os.getenv('lastfmkey')
lastfmsecret = os.getenv('lastfmsecret')
lastfmuser = os.getenv('lastfmuser')

def spotifySearch(search):
    search = search.replace(' ', '%20')
    response = requests.get(
        url=f'https://api.spotify.com/v1/search?q={search}&type=track',
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + requests.get(url='http://127.0.0.1:8000/spotify-access-token').json()['access_token']
        }
    )
    response = response.json()
    return {'image': response['tracks']['items'][0]['album']['images'][0]['url'],
            'artistlink': response['tracks']['items'][0]['artists'][0]['external_urls']['spotify'],
            'tracklink': response['tracks']['items'][0]['external_urls']['spotify']}

def getTopTracks():
    response = requests.get(
        url=f'http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={lastfmuser}&api_key={lastfmapikey}&format=json&period=7day&limit=5'
    )
    response = response.json()
    parseado = {
        'track1': {'song': response['toptracks']['track'][0]['name'], 
                'artist': response['toptracks']['track'][0]['artist']['name'],
                'timesplayed': response['toptracks']['track'][0]['playcount'],
                'data': spotifySearch(f'{response["toptracks"]["track"][0]["name"]} {response["toptracks"]["track"][0]["artist"]["name"]}')},
        'track2': {'song': response['toptracks']['track'][1]['name'],
                'artist': response['toptracks']['track'][1]['artist']['name'],
                'timesplayed': response['toptracks']['track'][1]['playcount'],
                'data': spotifySearch(f'{response["toptracks"]["track"][1]["name"]} {response["toptracks"]["track"][1]["artist"]["name"]}')},
        'track3': {'song': response['toptracks']['track'][2]['name'],
                'artist': response['toptracks']['track'][2]['artist']['name'],
                'timesplayed': response['toptracks']['track'][2]['playcount'],
                'data': spotifySearch(f'{response["toptracks"]["track"][2]["name"]} {response["toptracks"]["track"][2]["artist"]["name"]}')},
        'track4': {'song': response['toptracks']['track'][3]['name'],
                'artist': response['toptracks']['track'][3]['artist']['name'],
                'timesplayed': response['toptracks']['track'][3]['playcount'],
                'data': spotifySearch(f'{response["toptracks"]["track"][3]["name"]} {response["toptracks"]["track"][3]["artist"]["name"]}')},
        'track5': {'song': response['toptracks']['track'][4]['name'],
                'artist': response['toptracks']['track'][4]['artist']['name'],
                'timesplayed': response['toptracks']['track'][4]['playcount'],
                'data': spotifySearch(f'{response["toptracks"]["track"][4]["name"]} {response["toptracks"]["track"][4]["artist"]["name"]}')}
    }
    return parseado

def getTopAlbums():
    response = requests.get(
        url=f'http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user={lastfmuser}&api_key={lastfmapikey}&format=json&period=7day&limit=5'
    )
    response = response.json()
    parseado = {
        'album1': {
            'album': response['topalbums']['album'][0]['name'],
            'artist': response['topalbums']['album'][0]['artist']['name'],
            'timesplayed': response['topalbums']['album'][0]['playcount'],
        },
        'album2': {
            'album': response['topalbums']['album'][1]['name'],
            'artist': response['topalbums']['album'][1]['artist']['name'],
            'timesplayed': response['topalbums']['album'][1]['playcount'],
        },
        'album3': {
            'album': response['topalbums']['album'][2]['name'],
            'artist': response['topalbums']['album'][2]['artist']['name'],
            'timesplayed': response['topalbums']['album'][2]['playcount'],
        },
        'album4': {
            'album': response['topalbums']['album'][3]['name'],
            'artist': response['topalbums']['album'][3]['artist']['name'],
            'timesplayed': response['topalbums']['album'][3]['playcount'],
        },
        'album5': {
            'album': response['topalbums']['album'][4]['name'],
            'artist': response['topalbums']['album'][4]['artist']['name'],
            'timesplayed': response['topalbums']['album'][4]['playcount'],
        }
    }
    return parseado

def getTopArtists():
    response = requests.get(
        url=f'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={lastfmuser}&api_key={lastfmapikey}&format=json&period=7day&limit=5'
    )
    response = response.json()
    parseado = {
        'artist1': {
            'artist': response['topartists']['artist'][0]['name'],
            'timesplayed': response['topartists']['artist'][0]['playcount'],
        },
        'artist2': {
            'artist': response['topartists']['artist'][1]['name'],
            'timesplayed': response['topartists']['artist'][1]['playcount'],
        },
        'artist3': {
            'artist': response['topartists']['artist'][2]['name'],
            'timesplayed': response['topartists']['artist'][2]['playcount'],
        },
        'artist4': {
            'artist': response['topartists']['artist'][3]['name'],
            'timesplayed': response['topartists']['artist'][3]['playcount'],
        },
        'artist5': {
            'artist': response['topartists']['artist'][4]['name'],
            'timesplayed': response['topartists']['artist'][4]['playcount'],
        }
    }
    return parseado

def getRecentTracks():
    response = requests.get(
        url=f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={lastfmuser}&api_key={lastfmapikey}&format=json&limit=5'
    )
    response = response.json()
    parseado = {
        'track1': {
            'song': response['recenttracks']['track'][0]['name'],
            'artist': response['recenttracks']['track'][0]['artist']['#text'],
            'album': response['recenttracks']['track'][0]['album']['#text']
        },
        'track2': {
            'song': response['recenttracks']['track'][1]['name'],
            'artist': response['recenttracks']['track'][1]['artist']['#text'],
            'album': response['recenttracks']['track'][1]['album']['#text']
        },
        'track3': {
            'song': response['recenttracks']['track'][2]['name'],
            'artist': response['recenttracks']['track'][2]['artist']['#text'],
            'album': response['recenttracks']['track'][2]['album']['#text']
        },
        'track4': {
            'song': response['recenttracks']['track'][3]['name'],
            'artist': response['recenttracks']['track'][3]['artist']['#text'],
            'album': response['recenttracks']['track'][3]['album']['#text']
        },
        'track5': {
            'song': response['recenttracks']['track'][4]['name'],
            'artist': response['recenttracks']['track'][4]['artist']['#text'],
            'album': response['recenttracks']['track'][4]['album']['#text']
        }
    }
    return parseado