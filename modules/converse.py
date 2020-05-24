# Natural Language Toolkit: Chatbot Utilities
#
# Copyright (C) 2001-2019 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# Copyrights of nltk toolkit is preserved
# J,A.R.V.I.S created by Anirudha BS

from __future__ import print_function
import speech_recognition as sr
import pyttsx3
import re
import random
from six.moves import input
from modules.open import util_open
from modules.web_search import search

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    voice_id = "english-us" 
    engine.setProperty('voice', voice_id)
    engine.say(command)
    engine.runAndWait()

def gettext(MyText=""):

    try:

        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.5)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")

    return MyText


reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}


class Chat(object):

    def __init__(self, pairs, reflections={}):

        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def _compile_reflections(self):

        sorted_refl = sorted(self._reflections.keys(), key=len, reverse=True)
        return re.compile(
            r"\b({0})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE
        )

    def _substitute(self, str):

        return self._regex.sub(
            lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower()
        )

    def _wildcards(self, response, match):

        pos = response.find('%')
        while pos >= 0:
            num = int(response[pos + 1 : pos + 2])
            response = (
                response[:pos]
                + self._substitute(match.group(num))
                + response[pos + 2 :]
            )
            pos = response.find('%')
        return response

    def respond(self, str):

        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            if match:
                resp = random.choice(response)
                resp = self._wildcards(resp, match)

                if resp[-2:] == '?.':
                    resp = resp[:-2] + '.'
                if resp[-2:] == '??':
                    resp = resp[:-2] + '?'
                return resp


    def converse(self, quit="quit"):

        SpeakText("Hi, I'm Jarvis,Your personal assistant. You can say quit to leave")
        user_input = ""
        while user_input != quit:
            user_input = quit
            try:
                user_input = gettext()
            except EOFError:
                print(user_input)
            if user_input:
                respond=self.respond(user_input)
                if respond=="Searching web":
                    SpeakText("Searching the web for "+user_input.split()[-1])
                    search(user_input.split()[-1])
                elif respond=="Playing":
                    SpeakText("Playing "+user_input.split()[-1])
                    search(user_input.split()[-1])
                elif respond=="Opening":
                    SpeakText("Opening "+user_input.split()[-1])
                    util_open(user_input.split()[-1])
                else:
                    SpeakText(respond)
