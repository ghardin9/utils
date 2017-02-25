import requests

def test(address):
    paramcount = 8000
    data = {'name':'a'*paramcount}
    r = requests.get(address, params=data)
    while r.status_code != 414:
        if paramcount % 1000 == 0:
            print paramcount
        paramcount += 1
        data = {'name':'a'*paramcount}
        r = requests.get(address, params=data)
    return paramcount + 19


if __name__ == '__main__':
    address = 'http://54.202.82.13/'
    print test(address)
