
# when you make changes to the file you have to exit and enter interactive python again

import pprint
import json
tweets_str = '''[
    {"source": "Twitter Web Client",
        "id_str": "6312794445",
        "text": "Trump International Tower in Chicago ranked 6th tallest building in world by Council on Tall Buildings & Urban Habitat http://bit.ly/sqvQq",
        "created_at": "Thu Dec 03 19:39:09 +0000 2009",
        "retweet_count": 33,
        "favorite_count": 6
     },
    {"source": "Twitter Web Client",
        "id_str": "6971079756",
        "text": "From DONALD Trump: Wishing everyone a wonderful holiday & a happy, healthy, prosperous New Year. Let's think like champions in 2010!",
        "created_at": "Wed Dec 23 17:38:18 +0000 2009",
        "retweet_count": 28,
        "favorite_count": 12

     }
]
'''
'''
tweets = []
files = ['condensed_2009.json' ...]

for file in files:
    with open(file, encoding='ascii') as f:
        text = f.read()
        tweets += json.loads(text)
'''
'''
        tweets_str += f.read()
'''

tweets = json.loads(tweets_str)  # expects string as a variable

with open('condensed_2009.json', encoding='ascii') as f:
    tweets_str = f.read()
tweets = json.loads(tweets_str)
'''

# how many  tweets does Trump mention himself

num_trumps = 0
for tweet in tweets:
    # if Trump is talking about Trump
    if 'Trump' in tweet['text']:
        num_trumps += 1
print('num_trumps=', num_trumps)
print('percent=', num_trumps/len(tweets))
'''
