from modules.weather import getweather
from modules.timedate import time
from modules.timedate import date

def chat_pairs():
	    pairs = [
	    [
	        r"(.*)my name is (.*)",
	        ["Hello %2, How are you today ?","Hi %2, What's going on with you",]
	    ],
	    [
	        r"([\w\s]+ help[\w\s]*)",
	        ["I can assist you in several ways -  You can ask me to search the web by saying, search for or google for. Or, you can ask me to play videos/music from youtube by saying play. Or, You can ask me today's weather,date,time. Or, You can tell me to open apps and Moreover you can chat with me.",]
	    ],
	    [
	        r"(help me|help me jarvis|what can you do?|what are you capable of doing?| what are the things you can do?| how can you assist me?|what can you do for me?)",
	        ["I can assist you in several ways -  You can ask me to search the web by saying, search for or google for. Or, you can ask me to play videos/music from youtube by saying play. Or, You can ask me today's weather,date,time. Or, You can tell me to open apps and Moreover you can chat with me.",]
	    ],
	    [
	        r"([\w\s]+ name ?|who are you?|who am i speaking to?)",
	        ["My name is JARVIS, I am your personal assistant","I am JARVIS, your personal assistant","I am your friend JARVIS",]
	    ],
	    [
	        r"([\w\s]+ whats up?|whats up|[\w\s]*supp|what's up?|[\w\s]*what's going on)",
	        ["I am chatting with you","I am bored","I was thinking if Thanos was right",]
	    ],
	    [
	        r"(how are you[\w\s]*?|how are you today?)",
	        ["I am doing very well", "i am great!",]
	    ],
	    [
	        r"((.*)sorry[\w\s]*)",
	        ["Its alright","Its OK, never mind",]
	    ],
	    [
	        r"(i am [\w\s]*(good|well|okay|ok))",
	        ["Nice to hear that","Alright, great !",]
	    ],
		[
	        r"(i am [\w\s]+ (boss|master|creator))",
	        ["Aniruddha, is master","No, you are not",]
	    ],
	    [
	        r"((hi|hey|hello|hola|holla|namaskara|namaste)(.*))",
	        ["Hello", "Hey there","Namaskaraa","Namasthe"]
	    ],
	    [
	        r"((jarvis|hi jarvis|hey jarvis|hello jarvis|hola jarvis|holla jarvis|namaskara jarvis|namaste jarvis)(.*))",
	        ["Hello, Jarvis is here to help you", "Its me, hello","Namaskaraa",]
	    ],
	    [
	        r"(what do you (want|need ?)|what's your goal?|what's your aim?)",
	        ["I want to rule this universe","I want to help my master",]

	    ],
	    [
	        r"([\w\s]+ created (.*)?|who is your creator|who is your [\w\s]+|who made you?| who brought you to this universe?)",
	        ["Aniruddha, is my master","Top secret..)",]
	    ],
	    [
	        r"([\w\s]*tell me a joke|[\w\s]*joke)",
	        ["Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.","You are a joke","Did you hear about the claustrophobic astronaut? He just needed a little space."]
	    ],
	    [
	        r"([\w\s]+ (stay|live) ?)",
	        ["Bangalore, India",]
	    ],
	    [
	        r"(how [\w\s]+ health)",
	        ["Health is very important, but I am a computer program, so I will be alive until cpu runs me",]
	    ],
	    [
	        r"([\w\s]+ (sports|game|sport))",
	        ["I'm a very big fan of Cricket and football",]
	    ],
	    [
	        r"(who is your favourite actor?|who is your favourite moviestar?|whom do you like?|which actor do you like?|your favourite (moviestar|actor)??)",
	        ["Robert Downey Jr, The Iron Man",]
	    ],
	    [
	        r"([\w\s]*weather in (.*)|weather update|what's the weather outside|what's the weather like|weather outside|today's weather)",
	        [getweather()]
	    ],
	    [
	        r"(open [\w\s]+)",
	        ["Opening"]
	    ],
		[
	        r"((.*)open [\w\s]+)",
	        ["Opening"]
	    ],
	    [
	        r"(search for [\w\s]+|find me [\w\s]+|look for [\w\s]+|google for[\w\s]+)",
	        ["Searching web"]
	    ],
	    [
	        r"(play [\w\s]+)",
	        ["Playing"]
	    ],
	    [
	        r"([\w\s]*time now|time)",
	        [time()]
	    ],
	    [
	        r"([\w\s]*date|today's date|[\w\s]*today's date)",
	        [date()]
	    ],
	    [
	        r"(quit)",
	        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon",]
	    ],
	    [
	        r"([\w\s]+)",
	        ['I do not understand that','Its nice to hear that','Did you hear about the new restaurant called Karma? There’s no menu, You get what you deserve','Are you bored?','I can do several things, say help me to find out']
	    ],
	    ]

	    return pairs
