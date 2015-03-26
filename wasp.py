from dex import think
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 100)
import time
from dex import default

x = think()
engine.say('How Can i Help you Master. .?')
engine.runAndWait()
data = raw_input('How Can i Help you Master. .?' + '\n')
if 'how' in data and 'are' in data or 'how' in data and 'do' in data:
    print x.fine()
if 'news' in data:
    lang = raw_input('Which Language You want me to get for. .' '\n'
                     'Type 1 for Enhlish 2 for tamil''\n')
    if lang in ['1','2']:
        x.news(lang)
    else:
        engine.say( 'you know,Its not an option so Get me the language,then')
        engine.runAndWait()
elif 'who' in data and 'are' in data:
    x.whoareyou()
elif 'who' in data and 'am' in data:
    x.whoami()
elif 'joke' in data:
    x.jokes() 
elif 'personal' in data or ('about' in data and 'you' in data):
    data_p = raw_input('What you want now')
    x.defaults(str(data_p),default)
elif 'math' in data or 'maths' in data:
    m = raw_input('Gimme the Maths Problem. .!''\n')
    num01 = raw_input('1st number :')
    num02 = raw_input('2st number :')
    num1 = max(num01,num02)
    num2 = min(num01,num02)
    x.mathx(m,int(num1),int(num2))
   
else:
    print x.sorry()