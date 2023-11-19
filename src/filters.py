import re
import datetime

HTML_DEFAULT_CLASS = 'BasicTilestyles__Container'


def filter_characters(data):
    pattern = re.compile(rf"{HTML_DEFAULT_CLASS}.*")
    filtered = []
    for element in data:
        try:
            element_classes = element.get("class")
            for element_class in element_classes:
                match = pattern.match(element_class)
                if match:
                    element['name'] = element.get('h1').text
                    element['serie'] = element.get('paragraphs')[0]
                    paragraphs_size = len(element.get('paragraphs'))
                    if (paragraphs_size > 0):
                        element['available_date'] = format_available_date(
                            element.get('paragraphs')[
                                paragraphs_size - 1])
                    filtered.append(element)
        except TypeError as error:
            print('Error filtrado elemento por class ', error)
    return filtered


def format_available_date(available_date_str: str) -> datetime:
    available_date = None
    available_date_str = re.sub(r'[^0-9/]', '', available_date_str)
    match = re.match(
        r'^([0-9]{2})\/([0-9]{2})\/([0-9]{2})$', available_date_str)
    if match:
        available_date = datetime.datetime.strptime(
            available_date_str, "%d/%m/%y")
    else:
        available_date = is_only_yer_available(available_date_str)
    if available_date is not None:
        available_date = available_date.date()
    return available_date


def is_only_yer_available(available_date_str: str):
    match = re.match(r'^[0-9]{4}$', available_date_str)
    available_date = None
    if match:
        available_date_str = f'01/01/{available_date_str[2:]}'
        available_date = datetime.datetime.strptime(
            available_date_str, "%d/%m/%y")
    else:
        print('Formato incorrecto. No tiene ni el año.')
    return available_date
