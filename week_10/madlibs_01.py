import random
import praw
import time

from praw.reddit import Submission

madlibs = [
    "Thank you to [LEADER] for noticing my [GREAT] [ACHIEVEMENTS]. This is only the [BEGINNING] and we will [FIGHT] on to drain the [SWAP]",
    "It is time to fight [TYRANNY] through the means of [FORCE]! There is no [COUNTRY] that comes even close to [CHALLENGING] the [MIGHT] of the Unites State of America",
    "What is the meaning of this [CONFERENCE]? All I see is a [BUNCH] of [WEAKLINGS] with no sense of [DIRECTION] and capacity for [ACTION]",
    "[LOVE],[POWER] and [PERSEVERENCE] - that is my [MOTTO]. If you have a problem with that, I suggest you visit a [DOCTOR]",
    "No one can [CONTEMPLATE] [CURRENT] conditions without finding much that is satisfying and still more that is encouraging. Our own [COUNTRY]\
         is leading the world in the general readjustment to the results of the great conflict. Many of its [BURDENS] will bear heavily upon us for [YEARS],\
              and the secondary and indirect effects we must expect to experience for some time.",
    "There is something that I must say to my people, who stand on the warm threshold which leads into the palace of [JUSTICE]: In the process of gaining our [RIGHTFUL] place, \
        we must not be guilty of [WRONGFUL] deeds. Let us not seek to satisfy our [THIRST] for [FREEDOM] by drinking from the cup of bitterness and hatred.\
             We must forever conduct our struggle on the high plane of dignity and discipline. We must not allow our creative protest to degenerate into physical violence.\
                  Again and again, we must rise to the [MAJESTIC] heights of meeting physical force with [SOUL] force."
]

replacements = {
    'LEADER': ['Nancy Pelosi', 'Chuck Schumer', 'Vladimir Putin', 'Fidel Castro', 'Kim Jong-Un', 'Angela Merkel'],
    'GREAT': ['great', 'magnificent', 'fantastic', 'wonderful', 'blinding'],
    'ACHIEVEMENTS': ['war efforts', 'public speaking skills', 'commitment to this country', 'hair'],
    'BEGINNING': ['beginning', 'start', 'genesis', 'dawn', 'emergence'],
    'FIGHT': ['fight', 'grapple', 'brawl', 'struggle', 'duel'],
    'SWAP': ['swamp', 'marsh', 'bog', 'bayou', 'moor', 'wetland'],
    'TYRANNY': ['tyranny', 'communism', 'Russia', 'China'],
    'FORCE': ['depriving them from my excellence', 'force', 'blitzkrieg', 'overthrowing their weak and meager governemnt'],
    'CHALLENGING': ['challenging', 'testing', 'meeting', 'stretching', 'taxing'],
    'MIGHT': ['might', 'power', 'force', 'strength', 'energy', 'stamina', 'stoutness'],
    'CONFERENCE': ['conference', 'meeting', 'pointless debate', 'substandard political discussion thread'],
    'BUNCH': ['bunch', 'group', 'gathering', 'collective', 'mass'],
    'WEAKLINGS': ['weaklings', 'sissies', 'namby-pambys', 'cowards', 'pushovers', 'commies', 'softies', 'ninnies', 'doormats', 'chickens'],
    'DIRECTION': ['direction', 'determination', 'courage', 'guidance', 'leadership'],
    'ACTION': ['action', 'anything worth anything', 'deliberation', 'success'],
    'LOVE': ['Love', 'Kill', 'Adore', 'Learn', 'power'],
    'POWER': ['power', 'domination', 'weak central government', 'corporate interests', 'leader of the people'],
    'PERSEVERENCE': ['perseverence', 'power', 'greatness', 'force', ],
    'MOTTO': ['motto', 'decree', 'insigia', 'insight', 'maxim'],
    'DOCTOR': ['doctor', 'psychiatrist', 'Chairman Mao', 'Democratic Party', 'AA meeting'],
    'CONTEMPLATE': ['contemplate', 'ponder', 'consider', 'envisage', 'deliberate on'],
    'CURRENT': ['current', 'present', 'prevailing', 'existing', 'ongoing'],
    'COUNTRY': ['country', 'homeland', 'state', 'nation', 'community'],
    'BURDENS': ['burdens', 'problems', 'concerns', 'difficulties', 'hardship'],
    'YEARS': ['years', 'weeks', 'months' 'decades', 'centuries', 'millenia'],
    'JUSTICE': ['justice', 'righteousness', 'piousness', 'rectitude', 'truth'],
    'RIGHTFUL': ['rightful', 'promised', 'destined', 'just', 'true'],
    'WRONGFUL': ['wrongful', 'illegitimate', 'immoral', 'unfair', 'unlawful'],
    'THIRST': ['Thirst', 'desires', 'longing', 'appetite', 'hunger'],
    'FREEDOM': ['freedom', 'liberty', 'justice', 'opportunity', 'power'],
    'MAJESTIC': ['majestic', 'great', 'unimaginable', 'wholesome', 'immaculate'],
    'SOUL': ['soul', 'spiritual', 'justice', 'though', 'cause']


}


def generate_comment():

    s = random.choice(madlibs)
    for k in replacements.keys():
        s = s.replace('['+k+']', random.choice(replacements[k]))
    return(s)


reddit = praw.Reddit('botthehamhottspurs')
url = 'https://old.reddit.com/r/BotTown/comments/qr05je/practice_posting_messages_here/'
submission = reddit.submission(url=url)

# for i in range(75):
#   submission.reply(generate_comment())
#
#   time.sleep(30)

for comments in submission.comments.list():
    for i in range(25):
        print('comments=', comments)
        comments.reply(generate_comment())
        time.sleep(30)


for i in range(100):  # spam it for 100 times
    submission.comments[0].reply(generate_comment())
    submission.reply(generate_comment())
    print('made a comment, i = ', i)
    time.sleep(30)
