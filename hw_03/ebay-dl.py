from os import stat
from bs4 import BeautifulSoup as bs
import requests as req
import argparse as arg
import json
import csv


def parse_itemssold(text):
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0


def parse_shipping(text):
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if '$' in text:
        numbers = int(numbers)
        return numbers
    elif 'Free' in text:
        numbers = int(0)
        return numbers


def parse_price(text):  # creating the function that filters for only the price of the good
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if '$' in text:
        numbers = int(numbers)
        return numbers


def parse_status(text):  # creating the function that filters for the quality status of the good
    s = ''
    for char in text:
        s += char
    return s

    # get search term from the command line
parser = arg.ArgumentParser(description='Download from Ebay convert to JSON')
parser.add_argument('search_term')
parser.add_argument('--num_pages', default=10)
parser.add_argument('--csv', action='store_true')
args = parser.parse_args()
print('args.search_term=', args.search_term)

# list of all items found in all ebay webpages
items = []

# loop over the ebay webpages
for page_number in range(1, 11):

    # build the url
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + \
        args.search_term + '&_sacat=0&_pgn='+str(page_number)+'&rt=nc'
    #print('url=', url)

    # download the html
    r = req.get(url)
    status = r.status_code
    #print('status=', status)

    # download the html strings
    html = r.text

    #print('html=', html[0:20])

    # process the html
    soup = bs(html, 'html.parser')
    tag_items = soup.select('.s-item')

    #print('tags=', tag_items)
    for tag_item in tag_items:

        tags_names = tag_item.select('.s-item__title')  # get item title/name
        name = None
        for tag in tags_names:
            name = tag.text
            #print('tag_text=', name)

        free_return = False
        # find out whetherif item has free return or not
        tags_freereturn = tag_item.select('.s-item__free-returns')
        for tag in tags_freereturn:
            free_return = True

        items_sold = None
        tags_itemssold = tag_item.select('.s-item__hotness')
        for tag in tags_itemssold:
            items_sold = parse_itemssold(tag.text)

        shipping = None
        tags_shipping = tag_item.select(
            '.s-item__shipping')  # find the shipping fee
        for tag in tags_shipping:
            shipping = parse_shipping(tag.text)

        price = None
        # find the price of the good
        tags_price = tag_item.select('.s-item__price')
        for tag in tags_price:
            price = parse_price(tag.text)

        status = None
        # find the quality status of the good
        tags_status = tag_item.select('.SECONDARY_INFO')
        for tag in tags_status:
            status = parse_status(tag.text)

        # creating the dictionary
        item = {
            'name': name,
            'free_returns': free_return,
            'itemssold': items_sold,
            'shipping': shipping,
            'price': price,
            'status': status
        }
        items.append(item)

        # for item in items:
        #print('item=', item)

if args.csv:
    headings = ['name', 'price', 'status',
                'shipping', 'free_returns', 'itemssold']
    filename = args.search_term+'.csv'
    with open(filename, 'w', encoding='utf-8') as c:
        csv_writer = csv.DictWriter(c, headings)
        csv_writer.writeheader()
        csv_writer.writerows(items)
else:

    # writing dictionary into a JSON file
    filename = args.search_term+'.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))
