# Simple CSV to Django importer for the beer
# python manage.py shell
# from scripts import import_beer
# import_beer.run()
import csv
from beer.models import Beer


def run():
    # get the beers
    beers = csv.reader(open('durden_saucer.csv', 'rb'), delimiter=';')
    
    # import beers
    for beer in beers:
        b = Beer()
        b.name = beer[1]
        b.type = beer[2].lower()
        b.style = beer[3]
        b.description = beer[4]
        b.save()