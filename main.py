import tweepy as tw
import requests
import pandas as pd
import random

class User:
    def __init__(self, customer_key, customer_secret, access_token, access_secret, bearer):
        self.customer_key = customer_key
        self.customer_secret = customer_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.bearer = bearer

# Plug in your api credentials v
api_key = ""
api_key_secret = ""
api_access_token = ""
api_access_secret = ""
bearer = ""

id = "" # plug in twitter user id

user = User(customer_key=api_key,
            customer_secret=api_key_secret,
            access_token=api_access_token,
            access_secret=api_access_secret,
            bearer= bearer
            )

client = tw.Client(bearer_token=user.bearer,
                   consumer_key=user.customer_key,
                   consumer_secret=user.customer_secret,
                   access_token=user.access_token,
                   access_token_secret=user.access_secret,
                   return_type=requests.Response,
                   wait_on_rate_limit=True)


def factlist(filename, columnname:str):
    facts = pd.read_csv(filename)
    data = [i.replace(',', '') for i in facts[columnname]]
    return data


data = factlist(filename='data/Catfacts2.csv', columnname='catfacts')
facts = data


while True:
    factoftheday = random.choice(facts)
    if factoftheday not in list(client.get_users_tweets(id=id, since_id=1597318138693050369)):
        break

try:
    client.create_tweet(text=f'{factoftheday} #cat #catfact')
except:
    pass




