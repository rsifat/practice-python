import webbrowser as web

def webauto ():
    #edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS = (
        "youtube.com",
        "facebook.com",
        "google.com",
        "wikipedia.org"


    )

    for url in URLS:
        print("opening:"+ url)
        #web.get(edge_path).open(url)
        web.get(chrome_path).open(url)
       
      
webauto()