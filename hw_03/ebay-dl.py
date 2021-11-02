from bs4 import BeautifulSoup as bs
import requests as req
import argparse as arg

# get search term from the command line
parser = arg.ArgumentParser(description='Download from Ebay convert to JSON')
parser.add_argument('search_term')
parser.add_argument('--num_pages', default=10)
args = parser.parse_args()
print('args.search_term=', args.search_term)

# list of all items found in all ebay webpages
items = []

# loop over the ebay webpages
for page_number in range(1, 2):

    # build the url
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + \
        args.search_term + '&_sacat=0&_pgn='+str(page_number)+'&rt=nc'
    print('url=', url)

    # download the html
    r = req.get(url)
    status = r.status_code
    print('status=', status)
    html = r.text

    #print('html=', html[0:20])

    # process html

    soup = bs(html, 'html.parser')
    tags_name = soup.select('.s-item__link')
    #print('tags=', tags)

    tags_items = soup.select('.s-item')
    for tag_item in tags_items:

        tags_name = tag_item.select

       #print('tag_items=', tags_items)

    # for tag in tags_name:
    #   items.append({'name': tag.text})
    #  print('tag.text=', tag.text)

    #tags_freereturns = soup.select('.s-item__free-returns')
    # for tag in tags_freereturns:
    #   print('tag=', tag)

    #print('length', len(items))
    #print('free', len(tags_freereturns))
