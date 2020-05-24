import webbrowser

def search(query):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    for j in search(query, tld="co.in", num=1, stop=1, pause=1):
        a_website = j
        webbrowser.open_new(a_website)
