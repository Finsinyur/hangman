def WordBank():
	# Import modules required: excel, datetime and tweepy
	import tweepy
	
	i = 0
	wordBank = []
	# My Application Details
	consumer_key = "e6HuXQmHVlvteeKBJc31bmWjd"
	consumer_secret = "z6zR9wgXsUZmfVPkg5ge5j50lAVApljiOOVwoLVLsu25nd8UCH"
	access_token = "972836080717250565-IK6ejzed1nQowriRPkKMqm5dYfsV22S"
	access_token_secret = "uqbFXTXktWcw8posyt3hZSzbmi3RRHRYIUpkX5ao9xEt0"

	# Creating the authentication object
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	# Setting your access token and secret
	auth.set_access_token(access_token, access_token_secret)
	# Creating the API object while passing in auth information
	api = tweepy.API(auth) 

	# I want to extract tweets based on keyword provided
	# Request User for user input
	name = "PWPWordOTD"

	# Calling the user_timeline function with our parameters
	results = api.user_timeline(id=name, count=100)
	
	for tweet in results:
		word = tweet.text.split(" ")
		wordBank.append((word[0].lower()).rstrip(':'))

	return wordBank