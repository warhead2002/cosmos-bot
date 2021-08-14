from re import search
import discord
import os
import requests
import json
from bs4 import BeautifulSoup
import rand

client = discord.Client()

def cosmo(name,search):
    url = "https://api.le-systeme-solaire.net/rest/bodies/"+name

    r = requests.get(url)

    soup = BeautifulSoup(r.content,'html.parser')
    data = json.loads(soup.decode('utf-8'))

    if data['isPlanet'] == True:
        obj = 'Planet'
    else:
        obj = 'Non-Planet'
    start = ('Name of object: '+str(data['name']+'\n'))
    if search == 'type:':
        return('```'+start+'Type of object: '+obj+'```')
    if search == 'semi-major-axis':
        return('```'+start+'Semi Major Axis: '+str(data['semimajorAxis'])+' Km'+'```')
    if search == 'perihelion':
        return('```'+start+'Perihelion: '+str(data['perihelion'])+' Km'+'```')
    if search == 'aphelion':
        return('```'+start+'Aphelion: '+str(data['aphelion'])+'```')
    if search == 'eccentricity':
        return('```'+start+'Eccentricity: '+str(data['eccentricity'])+'```')
    if search == 'mass':
        return('```'+start+'Mass: '+str(data['mass']['massValue'])+' *10^'+data['mass']['massExponent']+' Kg'+'```')
    if search == 'density':
        return('```'+start+'Density: '+str(data['density'])+' Kg/m^3'+'```')
    if search == 'radius':
        return('```'+start+'Radius: '+str(data['meanRadius'])+' Km'+'```')
    if search == 'gravity':
        return('```'+start+'Gravity: '+str(data['gravity'])+' metre/second^2'+'```')
    if search == 'escape-velocity':
        return('```'+start+'Escape Velocity: '+str(data['escape'])+' metre/second'+'```')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Universe"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user_id = message.author.id

    g = ['Hello','Hola','Bonjour','Fuck off','Do not disturb']
    r = rand.rand()
    if r%2 == 0:
        greet = g[0]
    if r%3 == 0:
        greet = g[1]
    if r%5 == 0:
        greet = g[2]
    if r%7 == 0:
        greet = g[3]
    if r%13 == 0:
        greet = g[4]
    
    if message.content.startswith('$hello'):
        await message.channel.send(greet)
    if message.content.startswith('$daanish'):
        await message.channel.send('Hello daanish!')
    if message.content.startswith('cosmo info'):
        msg = '```'+'This is an educational bot that returns information \n about objects in our solar system to the user.\n Current Commands:\n cosmo [object name] [info required]\n eg:- cosmo mars gravity, returns gravity on Mars\n cosmo info directory:\n type,gravity,escape-velocty,perihelion,aphelion,\n semi-major-axis,eccentricity,mass,density,radius\n$hello , in case you are feeling lonely :P '+'```'
        await message.channel.send(msg)
    if message.content.startswith('$id'):
        await message.channel.send(user_id)
    if message.content.startswith('cosmo'):
        userMessage = message.content
        inp = str(userMessage[6:])
        ls = inp.split(' ')
        name = ls[0]
        search = ls[1]
        output = cosmo(name,search)
        await message.channel.send(output)
        return


client.run('Nzk5NTU3MDY4OTcyNzUyODk3.YAFTjA.FsuTWFIb2BLWVXuQcOgTlvLMGhY')