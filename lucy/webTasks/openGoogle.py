import webbrowser


def openGoogle():  
    '''
    openGoogle - To open google webpage in a New Tab
    '''    

    urL='https://www.google.com'
    edge_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open_new_tab(urL)

