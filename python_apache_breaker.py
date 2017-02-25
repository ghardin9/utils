import requests
import argparse

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
    parser = argparse.ArgumentParser()
    parser.add_argument("address",
                        help="choose a target website")
    args = parser.parse_args()
    address = args.address
    print test(address)
    
