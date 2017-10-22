import twitter
from decouple import config
from save_json import salvar

# using Python-Decouple for save keys
api = twitter.Api(consumer_key=config('consumer_key'),
                  consumer_secret=config('consumer_secret'),
                  access_token_key=config('access_token_key'),
                  access_token_secret=config('access_token_secret'))


users = api.GetUserTimeline(screen_name='jamesperes', count=200)

tweet = []
for key in users:
    tw = key.AsDict()
    created_at = tw["created_at"]
    id_tweet = tw["id"]
    text = tw["text"]
    dic = dict(created_at=created_at, id_tweet=id_tweet, text=text)
    tweet.append(dic)

salvar(tweet)
