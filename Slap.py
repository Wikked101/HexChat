from __future__ import print_function

from random import choice

import hexchat

__module_name__ = 'Slap'
__module_version__ = '0.1'
__module_description__ = 'Slaps someone'
__author__ = 'Wikked'

slaps = [
    'slaps {} around a bit with a large trout',
    'gives {} a clout round the head with a fresh copy of WeeChat',
    'slaps {} with a large smelly trout',
    'breaks out the slapping rod and looks sternly at {}',
    'slaps {}\'s bottom and grins cheekily',
    'slaps {} a few times',
    'slaps {} and starts getting carried away',
    'would slap {}, but is not being violent today',
    'gives {} a hearty slap',
    'finds the closest large object and gives {} a slap with it',
    'likes slapping people and randomly picks {} to slap',
    'dusts off a kitchen towel and slaps it at {}',
    'breaks a bottle on {}\'s head',
    'hits {} with every goldbar in fort knox',
    'hugs {} with a rather large squid',
    'waves at {} with a hydraulic pump',
    'slaps {} with a book by Stephen King',
    'inserts a 10mbit isa network card in {}',
    'slaps {} totally with a ladies handbag',
    'throws {} to a football team',
    'pours a bag of Cheerios into {}',
    'slaps {} with a hat',
    'slaps {} with the back hand',
    'throws a computer monitor at {}',
    'breaks a coconut open on {}\'s head',
    'yells at {} with a microfone',
    'breaks {}\'s cellphone with a dwarven axe',
    'hits {} with a stone',
    'throws a spiked club at {}',
    'slaps {} with a small asteroid, rich in iron',
    'hits {} with a small interstellar spaceship',
    'smears {} with a fresh zuccini',
    'slaps {} with a laptop',
    'hits {} with a big dictionary',
    'throws a baseball bat at {}',
    'kills {} with a mIRC script',
    'rubs {} with a tortoise',
    'kicks {} with a horse',
    'hits {} with the book of Kells',
    'feeds {} to a whale',
    'slaps {} with the New York Times Sunday Edition',
    'bites {} with a gnarly werewolf',
    'bites {} with a vampire',
    'puts {} into a perl script',
    'feeds {} with a bag of doggie chow',
    'slaps {} with a fat walrus',
    'hits {} with an IP address',
    'prays {} with a catholic priest',
    'slaps {} with James Dean',
    'throws {} to Ronald MacDonald',
    'runs {} trough Autoconf version 2.13',
    'slaps {} with a PRIVMSG',
    'spams {}\'s email address',
    'draws {} with some ANSI color codes',
    'attacks {} with a thermonuclear weapon',
    'reads to {} the hitch hikers guide to the galaxy, revised edition',
    'plays with {} and Nessie, the Loch Ness monster',
    'slaps {} with a tuna. Still in the can! *BONK* That will leave a mark',
    'burns {} with a red chinese dragon',
    'smears {} with a bird shit',
    'pours a tuborg super light beer down the throat on {}',
    'blows {} up with 1 ton of c4',
    'kills {} with the answer to everything',
    'blows {} away with a sandstorm',
    'jumps on {} with king kong',
    'bites {} with a donkey',
    'lets {} disappear into a black hole',
    'slaps {} with pure nothing',
    'stabs {} with a key',
    'slaps {} with an elevator',
    'chokes {} with a smiley printed in china',
    'hands {} a microsoft book',
    'slaps {} with a IPv6 IP address',
    'makes {} unstable with a 2.5 kernel',
    'slaps {} with bill gates wallet',
    'hugs {} with a carebear',
    'wraps {} with a 42m long worm',
    'smacks {} with Redhat 7',
    'slaps {} with Windows Update',
    'burries {} under an apple tree',
    'stings {} with all bees from a beehive'
]


def slap_cb(word, word_eol, userdata):
    if len(word) > 1:
        nick = word[1]
        hexchat.command('me ' + choice(slaps).format(nick))
    else:
        hexchat.command('help slap')
    return hexchat.EAT_ALL


def unload_cb(userdata):
    print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_command('slap', slap_cb, help='SLAP <nick>')
hexchat.hook_unload(unload_cb)
print(__module_name__, 'version', __module_version__, 'loaded.')
