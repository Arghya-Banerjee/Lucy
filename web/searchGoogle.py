import webbrowser


def searchGoogle(searchQuery):

    edge_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    searchQuery = str(searchQuery)
    searchString = searchQuery.replace(' ', '+')

    url = f"https://www.google.com/search?q={searchString}"

    # Example url = "https://www.google.com/search?q=birds+in+australia"

    webbrowser.get('edge').open(f"{url}")