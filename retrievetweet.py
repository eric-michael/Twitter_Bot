# Retrieve the latest tweet from specified user.

import requests
import time
from globals import api_search_url, bearer_token


# Filter the response to just the Tweet text.
def filter_text_from_response(res):
    full_results = res['results']
    latest_tweet = full_results[0]

    if latest_tweet['truncated']:
        extended_tweet = latest_tweet['extended_tweet']
        full_text = extended_tweet['full_text']
    else:
        full_text = latest_tweet['text']

    return full_text


def obtain_latest_tweet(user):

    current_day = time.strftime('"%Y%m%d0000"', time.localtime())
    current_time = time.strftime('"%Y%m%d%H%M"', time.localtime())

    headers = {
        'authorization': bearer_token,
        'Content-type': 'application/json',
    }
    data = '{"query":"from:' + user + ' lang:en","maxResults":"10","fromDate":' + current_day + ',"toDate":' \
           + current_time + '}'

    response = requests.post(api_search_url, headers=headers, data=data)

    print(response.text)

    full_text = filter_text_from_response(response.json())

    return full_text
