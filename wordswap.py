# Dictionary used to modify tweets

import urllib
from urllib import parse

basic_dict = {
    "are": "r",
    "be": "b",
    "because": "cuz",
    "come": "cum",
    "doing": "doin",
    "ever": "evr",
    "facts": "fax",
    "have": "hav",
    "hello": "sup",
    "hi": "yo",
    "high": "hi",
    "highest": "hiest",
    "highlight": "hilite",
    "hour": "hr",
    "hours": "hrs",
    "i": "ya boy",
    "know": "no",
    "light": "lite",
    "like": "lk",
    "people": "ppl",
    "picture": "pic",
    "pictures": "pics",
    "really": "rly",
    "tough": "tuff",
    "video": "vid",
    "videos": "vids",
    "what": "wut",
    "was": "wuz",
    "whom": "who",
    "you": "u",
    "your": "ur",
    "you're": "u r"
}


def word_swap(tweet):
    new_str = ''
    tweet = tweet.lower()
    split_tweet = tweet.split(' ')

    for x in split_tweet:
        if basic_dict.__contains__(x):
            new_str = new_str + ' ' + basic_dict[x]
        else:
            new_str = new_str + ' ' + x

    return urllib.parse.quote(new_str)
