import webbrowser


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