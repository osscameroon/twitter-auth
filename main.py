import tweepy
import configparser

CONFIGS = configparser.ConfigParser(interpolation=None)
CONFIGS.read("config.ini")

# Available from Twitter App
consumer_key = CONFIGS["AUTH"]["consumer_key"]
consumer_secret = CONFIGS["AUTH"]["consumer_secret"]


def authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, "oob")
    try:
        url = auth.get_authorization_url()
        print("auth url: ", url)

    except tweepy.TweepError:
        print("Error! Failed to get request token.")

    request_token = auth.request_token["oauth_token"]

    verifier = input("Verifier:")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.request_token = {"oauth_token": request_token, "oauth_token_secret": verifier}
    try:
        access_token = auth.get_access_token(verifier)
        print("api_key:", access_token[0])
        print("api_secret:", access_token[1])
    except tweepy.TweepError:
        print("Error! Failed to get access token.")


if __name__ == "__main__":
    authenticate()
