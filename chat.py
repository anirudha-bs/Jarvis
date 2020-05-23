from converse import Chat, reflections
from weather import getweather
from timedate import time
from timedate import date

pairs = [
    [
        r"(.*) my name is (.*)",
        ["Hello %2, How are you today ?","Hi %2, What's going on with you",]
    ],
    [
        r"(.*) help (.*)",
        ["I can assist you in several ways -  You can ask me search the web, or, I can play videos/music from youtube, or, You can ask me today's weather,date,time, or, You can tell me to open apps and Moreover you can chat with me.",]
    ],
    [
        r"help me",
        ["I can assist you in several ways -  You can ask me search the web, or, I can play videos/music from youtube, or, You can ask me today's weather,date,time, or, You can tell me to open apps and Moreover you can chat with me.",]
    ],
    [
        r"(.*) your name ?",
        ["My name is JARVIS","I am J.A.R.V.I.S","I am your friend JARVIS",]
    ],
    [
        r"what's up?",
        ["Nothing much","I am bored","I was thinking if Thanos was right",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great!",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla|namaskara|namaste)(.*)",
        ["Hello", "Hey there","Namaskara","Namaste"]
    ],
    [
        r"what (.*) want ?",
        ["I want to rule this universe",]

    ],
    [
        r"((.*)created(.*)|who is your creator)",
        ["Anirudha is my master","Top secret ;)",]
    ],
    [
        r"tell me a joke",
        ["Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.","You are a joke","Did you hear about the claustrophobic astronaut? He just needed a little space."]
    ],
    [
        r"(.*) (stay|location|city) ?",
        ["Bangalore, India",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I will be alive until battery backs me up",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket and football",]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Robert Downey Jr",]
    ],
    [
        r"((.*) weather in (.*)|weather update|what's the weather |what's the weather like)",
        [getweather()]
    ],
    [
        r"open (.*)",
        ["Opening"]
    ],
    [
        r"((search the web for (.*)|search for (.*) |find me (.*) |look for (.*) |google (.*)| search (.*)))",
        ["Searching web"]
    ],
    [
        r"play (.*)",
        ["Playing"]
    ],
    [
        r"((.*) time now|time)",
        [time()]
    ],
    [
        r"((.*) date|today's date|(.*) today's date)",
        [date()]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)",]
    ],
    [
        r"(.*)",
        ['Its nice to hear that','Hear about the new restaurant called Karma? There’s no menu, You get what you deserve','Are you bored?','I can do several things, say help to find out']
    ],
]

print("Hi, I'm Jarvis, Your personal assistant\nSay quit to leave")

chat = Chat(pairs, reflections)

chat.converse()
