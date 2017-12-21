# collect tweeter using stream in tweepy.

import tweepy

# replace with yours!
auth = tweepy.OAuthHandler('0oLHN****vCqHMTgf', 'PaCxNe1BeYDVTI2P********fPyApb0Ncgld0')
auth.set_access_token('3********************FoZNV4rou5D', 'NUz***********************OtE5')


from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('dataset/MajorCrimes.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#MajorCrimes']) #you can replace with anything!
