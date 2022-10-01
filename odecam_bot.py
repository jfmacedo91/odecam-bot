import discord
import os
import requests
from random import randint
from decouple import config
from googleapiclient.discovery import build

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

TOKEN = config('TOKEN')
YOUTUBE_API_KEY = config('YOUTUBE_API_KEY')

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
def get_db1_youtube_video_id(order):
  res = youtube.search().list(part = 'snippet', channelId = 'UCQ-8s5xln0mtxfOSoN3cXrw', order=order).execute()
  video_id = res['items'][0]['id']['videoId']
  return video_id

class OdecamClient(discord.Client):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    if message.author == client.user:
      return

    elif message.content.startswith('!comandos'):
      await message.channel.send(
      '**Comandos que podem ser utilizados no servidor:**'
      + os.linesep + '`!stack` - *Mostra as tecnologias que eu já estudei*'
      + os.linesep + '`!social` - *Mostra meus contatos*'
      + os.linesep + '`!mangas` - *Mostra minha coleção de mangás*'
      + os.linesep + '`!pegarpokemon` - *Mostra um Pokemon aleatório*'
      + os.linesep + '`!ultimovideodb1` - *Mostra o último vídeo do canal do Youtude da DB1*'
      + os.linesep + '`!videomaisvistodb1` - *Mostra o vídeo mais visto do canal do Youtude da DB1*'
      )

    elif message.content.startswith('!stack'):
      await message.channel.send(
      '**Essas são as tecnologias que eu já estudei:**'
      + os.linesep + '- HTML'
      + os.linesep + '- CSS / SASS'
      + os.linesep + '- JavaScript / TypeScript'
      + os.linesep + '- ReactJS'
      + os.linesep + '- Next.js'
      + os.linesep + '- Python'
      )

    elif message.content.startswith('!social'):
      await message.channel.send(
      '**Meus contatos:**'
      + os.linesep + '*Github* - https://github.com/jfmacedo91'
      + os.linesep + '*LinkedIn* - https://www.linkedin.com/in/jfmacedo91/'
      + os.linesep + '*E-mail* - jfmacedo91@gmail.com'
      + os.linesep + '*Discord* - jfmacedo#4344'
      )

    elif message.content.startswith('!mangas'):
      await message.channel.send(
      '**Minha coleção de mangás**:'
      + os.linesep + '- Bleach Remix - `02 Volumes`'
      + os.linesep + '- Burn The Witch - `01 Volume`'
      + os.linesep + '- Chainsaw Man - `09 Volumes`'
      + os.linesep + '- Death Note - *Black Edition* - `06 Volumes`'
      + os.linesep + '- Demon Slayer - *Kimetsu No Yaiba* - `27 Volumes`'
      + os.linesep + '- Hell´s Paradise -	`08 Volumes`'
      + os.linesep + '- Jujutsu Kaisen - *Batalha de Feiticeiros* -	`21 Volumes`'
      + os.linesep + '- Kaiju N.° 8 -	`03 Volumes`'
      + os.linesep + '- One Piece *3 em 1* - `04 Volumes`'
      + os.linesep + '- Spy X Family - `09 Volumes`'
      + os.linesep + '- The Promised Neverland - `20 Volumes`'
      )

    elif message.content.startswith('!pegarpokemon'):
      try:
        data = requests.get('https://pokeapi.co/api/v2/pokedex/1').json()
        allPokemon = len(data['pokemon_entries'])
        pokemonId = randint(1, allPokemon)
        pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{ pokemonId }').json()
        pokemon_id = pokemon['id']
        pokemon_name = pokemon['name']
        pokemon_image = pokemon['sprites']['other']['official-artwork']['front_default']
        embed = discord.Embed(
          title = f'Você capturou um { pokemon_name.upper() }',
          description = f'Número da pokedex #{ pokemon_id }'
        )
        embed.set_image(url = pokemon_image)
        await message.channel.send(embed = embed)
      except Exception as error:
        await message.channel.send('Ops... Deu alguma coisa errada!')
        print(error)

    elif message.content.startswith('!ultimovideodb1'):
      try:
        video_id = get_db1_youtube_video_id('date')
        await message.channel.send(f'https://www.youtube.com/watch?v={ video_id }')
      except Exception as error:
        await message.channel.send('Ops... Deu alguma coisa errada!')
        print(error)

    elif message.content.startswith('!videomaisvistodb1'):
      try:
        video_id = get_db1_youtube_video_id('viewCount')
        await message.channel.send(f'https://www.youtube.com/watch?v={ video_id }')
      except Exception as error:
        await message.channel.send('Ops... Deu alguma coisa errada!')
        print(error)

  async def on_member_join(self, member):
    guild = member.guild
    channel = self.get_channel(1024437683356971078)
    if guild.system_channel is not None:
      response = (f'Que bom ter você em nosso canal { guild.name } do Discord { member.mention }'
      + os.linesep + '**Comandos que podem ser utilizados no servidor:**'
      + os.linesep + '`!stack` - *Mostra as tecnologias que eu já estudei*'
      + os.linesep + '`!social` - *Mostra meus contatos*'
      + os.linesep + '`!mangas` - *Mostra minha coleção de mangás*'
      + os.linesep + '`!pegarpokemon` - *Mostra um Pokemon aleatório*'
      + os.linesep + '`!ultimovideodb1` - *Mostra o último vídeo do canal do Youtude da DB1*'
      + os.linesep + '`!videomaisvistodb1` - *Mostra o vídeo mais visto do canal do Youtude da DB1*'
      )

      await channel.send(f'{ member.mention } acabou de entrar no canal, Boas vindas!')
      await member.send(response)

client = OdecamClient(intents=intents)
client.run(TOKEN)