import csv


def writer_character(character):
    with open("data.csv", "a") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow([
            character.get('name'),
            character.get("serie"),
            character.get("available_date")
        ])
