import requests_betclic
from selectors import *

def app():
    for index, value in betclic_selectors_three.items():
        print(index)
        requests_betclic.odds_three_possibilities_betclic(url=value, sheet_name=index)
    for index, value in betclic_selectors_two.items():
        print(index)
        if index == 'ksw' or index == 'mlb':
            requests_betclic.odds_two_possibilities_betclic(url=value, sheet_name=index,
                                                            type_of_locator='div')
        else:
            requests_betclic.odds_two_possibilities_betclic(url=value, sheet_name=index)
