import requests

address = 'http://54.202.82.13/'
paramcount = 8000
data = {'name':'a'*paramcount}
r = requests.get(address, params=data)
while r.status_code != 414:
    if paramcount % 1000 == 0:
        print paramcount
    paramcount += 1
    data = {'name':'a'*paramcount}
    r = requests.get(address, params=data)
print paramcount + 19
