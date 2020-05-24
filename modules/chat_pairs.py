from modules.weather import getweather
from modules.timedate import time
from modules.timedate import date

def chat_pairs():
	    pairs = [
	    [
	        r"((.*) my name is (.*)|(.*) i'm (.*))",
	        ["Hello %2, How are you today ?","Hi %2, What's going on with you",]
	    ],
	    [
	        r"(.*)help (.*)",
	        ["I can assist you in several ways -  You can ask me to search the web by saying, search for or google for. Or, you can ask me to play videos/music from youtube by saying play. Or, You can ask me today's weather,date,time. Or, You can tell me to open apps and Moreover you can chat with me.",]
	    ],
	    [
	        r"help me",
	        ["I can assist you in several ways -  You can ask me to search the web by saying, search for or google for. Or, you can ask me to play videos/music from youtube by saying play. Or, You can ask me today's weather,date,time. Or, You can tell me to open apps and Moreover you can chat with me.",]
	    ],
	    [
	        r"((.*) your name ?|who are you|who am i speaking to|what are you)",
	        ["My name is JARVIS","I am JARVIS","I am your friend JARVIS",]
	    ],
	    [
	        r"((.*)whats up|(.*)supp|what's up|(.*) up|what's going on)",
	        ["I am chatting with you","I am bored","I was thinking if Thanos was right",]
	    ],
	    [
	        r"how are you (.*) ?",
	        ["I am doing very well", "i am great!",]
	    ],
	    [
	        r"(.*) sorry (.*)",
	        ["Its alright","Its OK, never mind",]
	    ],
	    [
	        r"i'm (.*) (good|well|okay|ok)",
	        ["Nice to hear that","Alright, great !",]
	    ],
	    [
	        r"(hi|hey|hello|hola|holla|namaskara|namaste)(.*)",
	        ["Hello", "Hey there","Namaskaraa","Namasthe"]
	    ],
	    [
	        r"(jarvis|hi jarvis|hey jarvis|hello jarvis|hola jarvis|holla jarvis|namaskara jarvis|namaste jarvis)(.*)",
	        ["Hello, Jarvis is here to help you", "Its me, hello","Namaskaraa",]
	    ],
	    [
	        r"(what (.*) want ?| what do you need)",
	        ["I want to rule this universe","I want to help my master",]

	    ],
	    [
	        r"((.*)created(.*)|who is your creator|who is your (.*))",
	        ["Aanniiruuddhhaa, is my master","Top secret ;)",]
	    ],
	    [
	        r"(tell me a joke|(.*) joke)",
	        ["Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.","You are a joke","Did you hear about the claustrophobic astronaut? He just needed a little space."]
	    ],
	    [
	        r"(.*) (stay|live) ?",
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
	        r"((.*) weather in (.*)|weather update|what's the weather |what's the weather like|weather outside)",
	        [getweather()]
	    ],
	    [
	        r"open (.*)",
	        ["Opening"]
	    ],
		[
	        r"(.*) open (.*)",
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
	        r"(.*) play (.*)",
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
	        ['I do not understand that','Its nice to hear that','Hear about the new restaurant called Karma? There’s no menu, You get what you deserve','Are you bored?','I can do several things, say help me to find out']
	    ],
	    ]

	    return pairs
