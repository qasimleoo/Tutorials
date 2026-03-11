import urllib.parse


url = 'https://sub.example.com/path/page.html;foo=1&foo2=2?id=123#anchor'

var = urllib.parse.urlparse(url)

# or alternatively you can use .split.. as it moves params part to path only
print(var)

var = urllib.parse.urlsplit(url)
print(var)