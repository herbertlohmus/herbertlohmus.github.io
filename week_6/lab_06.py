import json
tweets = []
files = ['condensed_2009.json', 'condensed_2010.json', 'condensed_2011.json', 'condensed_2012.json', 'condensed_2013.json',
         'condensed_2014.json', 'condensed_2015.json', 'condensed_2016.json', 'condensed_2017.json', 'condensed_2018.json']
for file in files:
    with open(file, encoding='ascii') as f:
        text = f.read()
        tweets += json.loads(text)

num_trumps = 0
num_russia = 0
num_obama = 0
num_fake_news = 0
num_mexico = 0
num_huge = 0
num_great = 0
num_incredible = 0
for tweet in tweets:
    # if Trump is talking about Trump:
    # if 'TRUMP' in tweet['text'] or 'trump' in tweet['text'] or 'Trump' in tweet['text']:
    if 'trump' in tweet['text'].lower():
        num_trumps += 1
    if 'russia' in tweet['text'].lower():
        num_russia += 1
    if 'obama' in tweet['text'].lower():
        num_obama += 1
    if 'mexico' in tweet['text'].lower():
        num_mexico += 1
    if 'fake news' in tweet['text'].lower():
        num_fake_news += 1
    if 'huge' in tweet['text'].lower():
        num_huge += 1
    if 'great' in tweet['text'].lower():
        num_great += 1
    if 'incredible' in tweet['text'].lower():
        num_incredible += 1

#print(num_incredible, num_great, num_huge)
# print(len(tweets))
print('trump=', num_trumps, 'russia=', num_russia, 'obama=',
      num_obama, 'fake news=', num_fake_news, 'mexico=', num_mexico)
# print('trump=', num_trumps/len(tweets), 'russia=', num_russia/len(tweets), 'obama=',
#    len(tweets), 'mexico=', num_mexico /
#    len(tweets), 'incredible=', num_incredible/len(tweets),
#   'great=', num_great/len(tweets), 'huge=', num_huge/len(tweets))"

#txt_trump = "trump:{:<.2%}".format(num_trumps/len(tweets))
#txt_russia = "russia:{:<.2%}".format(num_russia/len(tweets))
#txt_obama = "obama:{:<.2%}".format(num_obama/len(tweets))
#txt_fake_news = "fake news:{:<.2%}".format(num_fake_news/len(tweets))
#txt_mexico = "mexico:{:<.2%}".format(num_mexico/len(tweets))
#txt_incredible = "incredible:{:<.2%}".format(num_incredible/len(tweets))
#txt_great = "great:{:<.2%}".format(num_great/len(tweets))
#txt_huge = "huge:{:<.2%}".format(num_huge/len(tweets))
# print(txt_trump, txt_russia, txt_obama, txt_fake_news,
#     txt_mexico, txt_incredible, txt_great, txt_huge)

words = [['trump', (num_trumps/len(tweets))], ['russia', num_russia/len(tweets)], ['obama', num_obama/len(tweets)], ['fake news', num_fake_news /
                                                                                                                     len(tweets)], ['mexico', num_mexico/len(tweets)], ['incredible', num_incredible/len(tweets)], ['great', num_great/len(tweets)], ['huge', num_huge/len(tweets)]]


row = "|{country:<16s} | {percentage:.2%}|".format
print("Percentage of times a word appears in Trump's tweets ")
for c in words:
    print(row(country=c[0], percentage=c[1]))
