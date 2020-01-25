# Application that retrieves a tweet from a specified user and replaces certain words with txt-slang versions of
# the same word.

# Author: Eric Michael Hicks 2019

import twitterbotoauth
import retrievetweet
import posttweet
import wordswap
from globals import user, app_key, app_secret

# Obtain latest tweet
tweet = retrievetweet.obtain_latest_tweet(user)
tweet = wordswap.word_swap(tweet)

# Access token
oauth_tokens = twitterbotoauth.obtain_access_token(app_key, app_secret)
resource_owner_key = oauth_tokens.get('oauth_token')
resource_owner_secret = oauth_tokens.get('oauth_token_secret')


# Make the tweet
tweet_response = posttweet.post(app_key, app_secret, resource_owner_key, resource_owner_secret, tweet)
print(tweet_response.text)
