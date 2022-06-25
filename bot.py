import tweepy

auth = tweepy.OAuthHandler('XrRPLZgzX9mkgoE2IsIyuCvD7', '0oLGCukCRjmcGVPfjBoYlTJo5tTt3aw3nfRXiPBnjI6WaaMNy2')
auth.set_access_token('1540547653645115392-171T7hELHaIGepMiu5jK0x5XjWNCby', 'H660cU4If9Zr48Wz5fWCQLVai75xJeviPIFFn6GKSUj6H')

api = tweepy.API(auth, wait_on_rate_limit=True)

public_tweets=api.home_timeline()

print(public_tweets)