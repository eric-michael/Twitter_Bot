# These variables change based on your App and who you want to re-tweet.
# Consult the Twitter API on how to acquire these values.

# The user name of the user you want to retweet.
user = 'realDonaldTrump'

keys_file = open('keys', "r")

keys_list = keys_file.readlines()

app_key = keys_list[0].strip('\n')
app_secret = keys_list[1].strip('\n')
api_search_url = keys_list[2].strip('\n')
bearer_token = keys_list[3].strip('\n')
