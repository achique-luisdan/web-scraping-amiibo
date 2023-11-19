import requests
from bs4 import BeautifulSoup

from filters import filter_characters
from utils import writer_character

if __name__ == '__main__':
    response = requests.get('https://www.nintendo.com/es-mx/amiibo/line-up/')
    soup = BeautifulSoup(response.content, "html.parser")
    divs = soup.find_all('div')
    elements = []
    for div in divs:
        dictionary = {}
        attributes = div.attrs
        dictionary['h1'] = div.find('h1')
        dictionary['paragraphs'] = list(
            map(lambda p: p.text,  div.find_all('p')))
        for attribute, value in attributes.items():
            dictionary[attribute] = value
        elements.append(dictionary)

    characters = filter_characters(elements)
    print('PERSONAJES')
    for character in characters:
        writer_character(character)
        print(character.get('name'))
        print(character.get('serie'))
        print(character.get('available_date'))
        print('-----------------------------')
