Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> url = "https://github.com/miaoyingyy/f1.git"
>>> user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
>>> values = {'username' : 'cqc',  'password' : 'XXXX' }
>>> headers = { 'User-Agent' : user_agent }
>>> data = urllib.urlencode(values)
>>> request = urllib2.Request(url, data, headers)
>>> response = urllib2.urlopen(request)
>>> page = response.read()
>>> 
