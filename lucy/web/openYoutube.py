import webbrowser


def openYoutube():  
    '''
    openYoutube - To open Youtube in a New Tab
    '''    

    urL='https://www.youtube.com'
    edge_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open_new_tab(urL) 
