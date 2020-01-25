# Make the tweet

from requests_oauthlib import OAuth1Session

url = 'https://api.twitter.com/1.1/statuses/update.json?status='


def post(app_key, app_secret, resource_owner_key, resource_owner_secret, tweet):

    oauth = OAuth1Session(client_key=app_key,
                          client_secret=app_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

    return oauth.post(url + tweet)

