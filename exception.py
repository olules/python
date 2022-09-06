import requests

#using exceptions
def fetch_data(url):
    try:
        res=requests.get(url)
        res.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print('An error occured {}'.format(error))
fetch_data('')   

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError as e:
        print(f'ZeroDivisionError occured: {e}')     
    else:
        print(result)
divide(0,0)    