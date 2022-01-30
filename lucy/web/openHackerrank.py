import webbrowser


def openHackerRank():  
    '''
    openHackerRank - To open HackerRank dashboard in a New Tab
    '''    

    urL='https://www.hackerrank.com/dashboard'
    edge_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open_new_tab(urL)
