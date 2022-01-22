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

def searchGoogle(searchQuery):
    '''
    searchGoogle - Search for user input in google

    Args:
        searchQuery (string): What user wants to search in google
    '''    

    edge_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    searchQuery = str(searchQuery)
    searchString = searchQuery.replace(' ', '+')

    url = f"https://www.google.com/search?q={searchString}"

    # Example url = "https://www.google.com/search?q=birds+in+australia"

    webbrowser.get('edge').open(f"{url}")

def searchYoutube(searchQuery):
    '''
    searchYoutube - Takes user input returns its in browser

    Args:
        searchQuery (string): What the user wants to search in Youtube
    '''    

    edge_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    searchQuery = str(searchQuery)
    searchString = searchQuery.replace(' ', '+')

    url = f"https://www.youtube.com/results?search_query={searchString}"

    # Example url = "https://www.youtube.com/results?search_query=bird+in+india"

    webbrowser.get('edge').open(f"{url}")

def searchYoutube(searchQuery):
    '''
    searchYoutube - Takes user input returns its in browser

    Args:
        searchQuery (string): What the user wants to search in Youtube
    '''    

    edge_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    searchQuery = str(searchQuery)
    searchString = searchQuery.replace(' ', '+')

    url = f"https://www.youtube.com/results?search_query={searchString}"

    # Example url = "https://www.youtube.com/results?search_query=bird+in+india"

    webbrowser.get('edge').open(f"{url}")


if __name__ == '__main__':

    openGoogle()
    openYoutube()
    openHackerRank()
    searchGoogle()
    searchYoutube()
    