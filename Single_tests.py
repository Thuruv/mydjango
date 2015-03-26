import string
import pyttsx
import requests
import feedparser
import random

x = ['No Joke Today','I am running out of Jokes','Am i your PA?','Shut Up']
engine = pyttsx.init()
engine.setProperty('rate', 80)

def jokes():
    term = random.randint(1, len(x)-1)
    engine.say(x[term])
    print x[term]

jokes()
