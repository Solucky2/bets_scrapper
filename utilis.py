from bs4 import BeautifulSoup
import requests
import pandas as pd
from itertools import zip_longest


def web_parser(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def betclic_oddvalues(soup):
    odd_values = soup.find_all('span', class_='oddValue')
    odd_values_list = [value.text for value in odd_values]
    return odd_values_list


def betclic_span_names(soup):
    players_names = soup.find_all('span', class_='scoreboard_contestantLabel')
    players_names_list = [value.text for value in players_names]
    return players_names_list


def betclic_div_names(soup):
    clubs_names = soup.find_all('div', class_='scoreboard_contestantLabel')
    clubs_names_list = [value.text for value in clubs_names]
    return clubs_names_list


def data_frame_two_possibilities(players_names_list, odd_values_list):
    cleaned_names_list = []
    for name in players_names_list:
        cleaned_name = name.strip().replace('\n', '').replace('                ', '')
        cleaned_names_list.append(cleaned_name)
    cleaned_odds_list = []
    for odd in odd_values_list:
        cleaned_odd = odd.strip().replace('-', '1,0')
        cleaned_odds_list.append(cleaned_odd)
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    for index, value in enumerate(cleaned_odds_list):
        if index % 2 == 0:
            if index < len(cleaned_names_list):
                column1.append(cleaned_names_list[index])
                column2.append(value)
        else:
            if index < len(cleaned_names_list):
                column3.append(cleaned_names_list[index])
                column4.append(value)

    data = {
        'Zawodnik1': column1,
        'Kurs1': column2,
        'Zawodnik2': column3,
        'Kurs2': column4
    }
    df = pd.DataFrame(data)
    if df.empty:
        print('There was a problem with loading a page, check if it still exists')
    return df


def rows_iterate_two_possibilities(df):
    proccessed_odds = []
    value_column = []
    for index, row in df.iterrows():
        try:
            value = 1 / float(row['Kurs1'].replace(',', '.')) + 1 / float(row['Kurs2'].replace(',', '.'))
            value_column.append(value)
            if value < 1:
                proccessed_odds.append(row['Zawodnik1'] + '/' + row['Zawodnik2'] + '/' + str(value))
            else:
                continue
        except ValueError:
            continue
    df.insert(len(df.columns), 'Wartość_Zwrotu', value_column)
    if len(proccessed_odds) > 0:
        print('Scrapped, found odds below 1.0')
        return df, '\n', proccessed_odds
    else:
        print("Scrapped, no odds below 1.0")
        return df


def rows_iterate_three_possibilities(df):
    proccessed_odds = []
    value_column = []
    for index, row in df.iterrows():
        try:
            value = 1 / float(row['Wygrana1'].replace(',', '.')) \
                + 1 / float(row['Remis'].replace(',', '.')) \
                + 1 / float(row['Wygrana2'].replace(',', '.'))
            value_column.append(value)
            if value < 1:
                proccessed_odds.append(row['Klub1'] + '/' + row['Klub2'] + '/' + str(value))
            else:
                continue
        except ValueError:
            continue
    try:
        df.insert(len(df.columns), 'Wartość_Zwrotu', value_column)
    except ValueError:
        print(f'There was a problem with scrapping, try again in couple more minutes')
        return 0

    if len(proccessed_odds) > 0:
        print("Scrapped, found odds below 1.0")
        return df, '\n', proccessed_odds
    else:
        print("Scrapped, no odds below 1.0")
        return df


def data_frame_three_possibilities(clubs_name_list, odd_values_list):
    cleaned_clubs_names_list = []
    for club_name in clubs_name_list:
        cleaned_name = club_name.strip().replace('\n', '').replace('                ', '')
        cleaned_clubs_names_list.append(cleaned_name)
    cleaned_odds_list = []
    for odd in odd_values_list:
        cleaned_odd = odd.strip().replace('-', '1,0')
        cleaned_odds_list.append(cleaned_odd)
    column1 = []  # nazwa1
    column2 = []  # nazwa2
    column3 = []  # wygrana1
    column4 = []  # remis
    column5 = []  # wygrana2

    for index in range(len(cleaned_clubs_names_list)):
        if index % 2 == 0:
            column1.append(cleaned_clubs_names_list[index])
        else:
            column2.append(cleaned_clubs_names_list[index])

    for index in range(len(cleaned_odds_list)):
        if index % 3 == 0:
            if len(cleaned_odds_list[index]) < 6:
                column3.append(cleaned_odds_list[index])
        elif index % 3 == 1:
            column4.append(cleaned_odds_list[index])
        else:
            column5.append(cleaned_odds_list[index])

    data = zip_longest(column1, column2, column3, column4, column5, fillvalue='1,0')
    df = pd.DataFrame(data, columns=['Klub1', 'Klub2', 'Wygrana1', 'Remis', 'Wygrana2'])
    if df.empty:
        print('There was a problem with loading a page, check if it still exists')
    return df


def save_to_excel(df, path, sheet_name):
    try:
        with pd.ExcelWriter(path, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    except FileNotFoundError:
        df.to_excel(path, sheet_name=sheet_name, index=False)
