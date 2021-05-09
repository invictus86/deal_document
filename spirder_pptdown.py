# import urllib2
#
# response = urllib2.urlopen('https://down.ypppt.com/uploads/soft/210318/1-21031R21331.zip')
# zipcontent = response.read()
# with open("log.zip", 'w') as f:
#     f.write(zipcontent)


import requests
res = requests.get('https://down.ypppt.com/uploads/soft/210318/1-21031R21331.zip')
print(res.content)
