import string
import pyttsx
import requests
import feedparser
import random
import time

default = {
    'prefers_email': False,
    'location': 'madras',
    'time': time.ctime(),
    'phone': '+91 -9962552414'
}


def enews():
    rss = 'http://www.thehindu.com/?service=rss'
    feed = feedparser.parse(rss)
    for key in feed["entries"][:10]: 
        print key["title"] + '\n'

def tnews():
    rss = 'http://tamil.thehindu.com/?service=rss'
    feed = feedparser.parse(rss)
    for key in feed["entries"][:10]: 
        print key["title"] + '\n'

x = ['No Joke Today','I am running out of Jokes','Am i your PA?']
engine = pyttsx.init()
engine.setProperty('rate', 80)
class think(object):

    def _init_(self):
        print 'What to think. .?'

    def ask(self):
        print 'What to ask. .?'

    def fine(self):
        engine.say("Fine,Cheif")
        engine.runAndWait()

    def sorry(self):
        engine.say("Sorry,Master I Can't get You")
        engine.runAndWait()

    def news(self,lang):
        
        engine.say("Here's what i got. .")
        print '---------------------------------------------'
        if lang == '1':
            print enews()
        elif lang == '2':
            print tnews()
        print '---------------------------------------------'
        engine.runAndWait()

    def whoareyou(self):
        engine.say("I'm Dexter")
        engine.runAndWait()

    def whoami(self):
        engine.say("You're My Kind ,are't you")
        engine.runAndWait()
        
    def jokes(self):
        term = random.randint(1, len(x)-1)
        engine.say(x[term])

    def defaults(self,getdata,default):
        print default['time']
        for word in getdata:
            if word.lower() in default.keys():
                print default[word]
    def mathx(self,mathdata,num1,num2):
        if 'add' in mathdata or 'subtract' in mathdata or 'multiply' in mathdata or 'divide' in mathdata:
            if 'add' in mathdata:
                print num1 + num2
            elif 'subtract' in mathdata:
                print num1-num2
            elif 'multiply' in mathdata:
                print num1 * num2
            elif 'divide' in mathdata:
                print num1 / num2
        else:
           print ( "Perhaps my Mathematical part of brain is malfunctioning.")
