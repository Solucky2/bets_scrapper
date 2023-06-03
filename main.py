from requests_betclic import *
from selectors import *

if __name__ == '__main__':
    for index, value in betclic_selectors_three.items():
        odds_three_possibilities_betclic(url=value, sheet_name=index)
    for index, value in betclic_selectors_two.items():
        if index == 'ksw':
            odds_two_possibilities_betclic(url=value, sheet_name=index,
                                           type_of_locator='div')
        else:
            odds_two_possibilities_betclic(url=value, sheet_name=index)
