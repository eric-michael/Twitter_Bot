# Oauth1 3-way handshake for obtaining an access token for authorizing requests.

from requests_oauthlib import OAuth1Session


def obtain_access_token(app_key, app_secret):
    # Credentials/URLs.
    request_token_url = 'https://api.twitter.com/oauth/request_token'
    auth_url_prefix = 'https://api.twitter.com/oauth/authorize'
    access_token_url = 'https://api.twitter.com/oauth/access_token'

    # Request token.
    auth = OAuth1Session(app_key, client_secret=app_secret)
    request_token_response = auth.fetch_request_token(request_token_url)
    resource_owner_key = request_token_response.get('oauth_token')
    resource_owner_secret = request_token_response.get('oauth_token_secret')

    # Obtain authorization from the user.
    authorization_url = auth.authorization_url(auth_url_prefix)
    print(authorization_url)
    redirect_response = input('Paste the redirect URL here: ')
    oauth_response = auth.parse_authorization_response(redirect_response)
    verifier = oauth_response.get('oauth_verifier')

    # Obtain access token.
    auth = OAuth1Session(app_key,
                         client_secret=app_secret,
                         resource_owner_key=resource_owner_key,
                         resource_owner_secret=resource_owner_secret,
                         verifier=verifier)
    oauth_tokens = auth.fetch_access_token(access_token_url)
    return oauth_tokens
