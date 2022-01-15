import webbrowser

def openGoogle():  
    '''
    openGoogle - To open google webpage in a New Tab
    '''    

    urL='https://www.google.com'
    edge_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open_new_tab(urL)

def openYoutube():  
    '''
    openYoutube - To open Youtube in a New Tab
    '''    

    urL='https://www.youtube.com'
    edge_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open_new_tab(urL) 

def openHackerRank():  
    '''
    openHackerRank - To open HackerRank dashboard in a New Tab
    '''    

    urL='https://www.hackerrank.com/dashboard'
    edge_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open_new_tab(urL)

if __name__ == '__main__':

    openGoogle()
    openYoutube()
    openHackerRank()
    