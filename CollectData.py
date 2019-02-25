import tweepy
import csv
#input your credentials her
consumer_key = 'abc'
consumer_secret = 'pqr'
access_token = 'xyz'
access_token_secret = 'lmn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
def recent():
	lis=[]
	for tweet in tweepy.Cursor(api.search,q="#demonetisation"+" -filter:retweets",count=10000,lang="en",since="2019-01-02").items():
		lis.append(tweet.text.encode('utf-8'))

	return lis


if __name__=="__main__":
	# Open/Create a file to append data
	csvFile = open('twitterdata.csv', 'w')
	# #Use csv Writer
	csvWriter = csv.writer(csvFile)

	for tweet in tweepy.Cursor(api.search,q="#demonetisation"+" -filter:retweets",count=10000,
	                           lang="en",
	                           since="2017-01-03").items():
	    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
	csvFile.close()

	
