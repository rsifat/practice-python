import webbrowser as web

def webauto ():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS = (
        "youtube.com",
        "facebook.com",
        "wikipedia.org",
        "google.com"
    )

    for url in URLS:
        print("opening:"+ url)
        web.get(chrome_path).open(url)
      
webauto()
