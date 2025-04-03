# LastFM Tracker

  

Primeiro de tudo, clona o repo, seta aquele venv do python e dá um pip install -r requirements.txt.

Ok, coisa linda, agora cria um .env na pasta raiz do repo

Nele você vai botar:

- clientid = '(insira sua api key do spotify)'

- secretid = '(insira seu secret do spotify)'

- refreshtoken = '(pega essa merda aqui https://spotify-refresh-token-generator.netlify.app/#info)'

- lastfmkey = '(insira sua api key do lastfm)'

- lastfmsecret = '(insira seu secret do lastfm)'

- tokenendpoint = 'https://accounts.spotify.com/api/token'

- currentlyplaying = 'https://api.spotify.com/v1/me/player/currently-playing'

- lastfmuser = '(insira user do lastfm)'

Fez isso, só entrar na pasta principal e rodar um ```uvicorn main:app```

Loucura, né? Pega o ip que ele vai te retornar e é isso.

As requisições disponíveis são:

- /spotify-access-token

  - Retorna o access token do spotify.

- /spotify-now-playing

  - Retorna o que você está escutando no spotify no momento. É meio ruim mas é o que há.

- /spotify-refresh-token

  - Retorna o refresh token do spotify.

- /search/(sua busca)

  - Retorna alguns dados de uma música no spotify.

- /lastfm-top-tracks

  - Retorna as top 5 musicas mais escutadas do seu perfil do lastfm nos últimos 7 dias.

- /lastfm-top-albums

  - Retorna os top 5 albuns mais escutados do seu perfil do lastfm nos últimos 7 dias.

- /lastfm-top-artists

  - Retorna os top 5 artistas mais escutados do seu perfil do lastfm nos últimos 7 dias.

- /lastfm-recent-tracks

  - Retorna as 5 últimas músicas escutadas do seu perfil do lastfm.

É basicamente isso, eu não sou nenhum mestre em API e isso foi feito pra aprendizado, espero que tenha ficado bom o suficiente :D
