import webbrowser
from googlesearch import search

def web_search(query):

    try:
        for j in search(query, tld="co.in", num=1, stop=1, pause=1):
            a_website = j
            return webbrowser.open_new(a_website)
    except:
    	return 0
