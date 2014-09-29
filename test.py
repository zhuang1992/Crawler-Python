import urllib

data={}
data['word']='Jecvay Notes'

url_values=urllib.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values

data=urllib.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)
