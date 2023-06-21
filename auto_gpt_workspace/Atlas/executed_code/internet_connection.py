import urllib.request

try:
    urllib.request.urlopen('https://www.google.com')
    print('Internet connection is working.')
except:
    print('Internet connection is not working.')