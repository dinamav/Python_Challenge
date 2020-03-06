import urllib.request
with urllib.request.urlopen("http://www.google.com") as url:
    s = url.read()
    print('here')