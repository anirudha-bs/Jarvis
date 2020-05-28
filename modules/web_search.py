import re
import webbrowser
from googlesearch import search

def play(query):

    try:
        for i in search(query, tld="co.in", num=10, stop=10, pause=0.5):
            if re.findall("youtube+", i):
                a_website = i
                return webbrowser.open_new(a_website)

    except:
        return 0

def google_search(query):

    try:
        search="https://www.google.co.in/search?q=" + query
        return webbrowser.open_new(search)
    except:
        return 0
