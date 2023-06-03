from requests_betclic import *
from selectors import *

if __name__ == '__main__':
    odds_two_possibilities_betclic(url=BetclicSelectorsTwo().betclic_tenis_url,
                                   sheet_name='tenis')
    odds_two_possibilities_betclic(url=BetclicSelectorsTwo().betclic_ksw_url, type_of_locator='div',
                                   sheet_name='ksw')
    odds_three_possibilities_betclic(url=BetclicSelectorsThree().betclic_serieA_url,
                                     sheet_name='serieA')
