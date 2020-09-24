import gzip
from array import array
# import random
# import time
# import itertools
import pkg_resources
import re

_card_regex = re.compile(r'[2-9tjqk][cdhs]', re.IGNORECASE)

HANDTYPES = [
    "invalid hand",
    "high card",
    "one pair",
    "two pairs",
    "three of a kind",
    "straight",
    "flush",
    "full house",
    "four of a kind",
    "straight flush"
]

CARDS = {
    "2c": 1,
    "2d": 2,
    "2h": 3,
    "2s": 4,
    "3c": 5,
    "3d": 6,
    "3h": 7,
    "3s": 8,
    "4c": 9,
    "4d": 10,
    "4h": 11,
    "4s": 12,
    "5c": 13,
    "5d": 14,
    "5h": 15,
    "5s": 16,
    "6c": 17,
    "6d": 18,
    "6h": 19,
    "6s": 20,
    "7c": 21,
    "7d": 22,
    "7h": 23,
    "7s": 24,
    "8c": 25,
    "8d": 26,
    "8h": 27,
    "8s": 28,
    "9c": 29,
    "9d": 30,
    "9h": 31,
    "9s": 32,
    "tc": 33,
    "td": 34,
    "th": 35,
    "ts": 36,
    "jc": 37,
    "jd": 38,
    "jh": 39,
    "js": 40,
    "qc": 41,
    "qd": 42,
    "qh": 43,
    "qs": 44,
    "kc": 45,
    "kd": 46,
    "kh": 47,
    "ks": 48,
    "ac": 49,
    "ad": 50,
    "ah": 51,
    "as": 52
}

INV_CARDS = {v: k for k, v in CARDS.items()}


def getcards(hand):
    if isinstance(hand, list):
        return [c for h in hand for c in getcards(h)]
    return [CARDS[str.lower(c)] for c in _card_regex.findall(hand)]


def gethand(cards, compress=False):
    sep = ' ' if not compress else ''
    return sep.join([INV_CARDS[c].capitalize() for c in cards])


def eval7(cards):
    p = 53
    for c in cards:
        p = _ranks[p + c]
    return p


def eval5(cards):
    p = 53
    for c in cards:
        p = _ranks[p + c]
    p = _ranks[p]
    return p


eval6 = eval5


def evalany(cards):
    p = 53
    for c in cards:
        p = _ranks[p + c]
    if 5 <= len(cards) <= 6:
        p = _ranks[p]
    return p


def rankinfo(p):
    return {
        "type": p >> 12,
        "rank": p & 0x00000fff,
        "value": p,
        "name": HANDTYPES[p >> 12]
    }

_stream = pkg_resources.resource_stream(__name__, 'data/HandRanks.dat.gz')

with gzip.GzipFile(fileobj=_stream) as f:
    _ranks = array('I')
    _ranks.fromfile(f, 32487834)
