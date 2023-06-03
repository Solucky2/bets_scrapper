from utilis import *
from constants import *


def odds_two_possibilities_betclic(url: str, sheet_name: str, type_of_locator='span'):
    soup = web_parser(url)
    odd_values_list = betclic_oddvalues(soup)
    players_names_list = betclic_span_names(soup)
    if type_of_locator == 'div':
        players_names_list = betclic_div_names(soup)
    df = data_frame_two_possibilities(players_names_list, odd_values_list)
    rows_iterate_two_possibilities(df)
    save_to_excel(df, path=file_path, sheet_name=sheet_name)


def odds_three_possibilities_betclic(url: str, sheet_name: str, type_of_locator='div'):
    soup = web_parser(url)
    odd_values_list = betclic_oddvalues(soup)
    clubs_name_list = betclic_div_names(soup)
    if type_of_locator == 'span':
        clubs_name_list = betclic_span_names(soup)
    df = data_frame_three_possibilities(clubs_name_list, odd_values_list)
    rows_iterate_three_possibilities(df)
    save_to_excel(df, path=file_path, sheet_name=sheet_name)
