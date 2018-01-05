# -*- coding:utf-8 -*-
import urllib
import urllib2
import re



user_agent = 'Mozilla/5.0 (Windows NT 6.1)'
headers = { 'User-Agent' : user_agent }
for page in range (1,2019):
    url = 'http://www.xxhh.com/duanzi/page/'+str(page)

    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason 

    content_pattern = re.compile('<div class="user-info">.*?<a href=".*?" title=".*?" target="_blank">(.*?)</a>', re.S)
    content_pattern1 = re.compile('<pre>(.*?)</pre>', re.S)
    content_list = re.findall(content_pattern, html)
    content_list1 = re.findall(content_pattern1, html)

    for item1 in content_list1:
        for item in content_list:
            print item
            del content_list[0]
            print '\n'
            break
        print item1
        print '\n'
           
    input = raw_input()    
    if input == "Q":       
        break
    print "******************************下一页******************************\n"
         
