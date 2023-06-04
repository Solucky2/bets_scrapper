import utilis
import constants


def odds_two_possibilities_betclic(url: str, sheet_name: str, type_of_locator='span'):
    soup = utilis.web_parser(url)
    odd_values_list = utilis.betclic_oddvalues(soup)
    players_names_list = utilis.betclic_span_names(soup)
    if type_of_locator == 'div':
        players_names_list = utilis.betclic_div_names(soup)
    df = utilis.data_frame_two_possibilities(players_names_list, odd_values_list)
    utilis.rows_iterate_two_possibilities(df)
    utilis.save_to_excel(df, path=constants.file_path, sheet_name=sheet_name)


def odds_three_possibilities_betclic(url: str, sheet_name: str, type_of_locator='div'):
    soup = utilis.web_parser(url)
    odd_values_list = utilis.betclic_oddvalues(soup)
    clubs_name_list = utilis.betclic_div_names(soup)
    if type_of_locator == 'span':
        clubs_name_list = utilis.betclic_span_names(soup)
    df = utilis.data_frame_three_possibilities(clubs_name_list, odd_values_list)
    utilis.rows_iterate_three_possibilities(df)
    utilis.save_to_excel(df, path=constants.file_path, sheet_name=sheet_name)
